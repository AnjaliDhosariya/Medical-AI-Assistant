import os
import time
from pathlib import Path
from dotenv import load_dotenv
from tqdm.auto import tqdm
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from pinecone import Pinecone,ServerlessSpec
from langchain.text_splitter import RecursiveCharacterTextSplitter



pdf_path = r"E:/Downloads/DIABETES.pdf"
loader = PyPDFLoader(pdf_path)
docs = loader.load()
print(docs[0].page_content)

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = "us-east-1"
PINECONE_INDEX_NAME = "medical-index"

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

UPLOAD_DIR = "./uploaded_docs"
os.makedirs(UPLOAD_DIR,exist_ok=True)

#initialise pinecone instance

pc = Pinecone(api_key=PINECONE_API_KEY)
spec = ServerlessSpec(cloud="aws", region=PINECONE_ENV)
existing_indexes = [i["name"] for i in pc.list_indexes()]

if PINECONE_INDEX_NAME not in existing_indexes:
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=768,  # Dimension of the embeddings
        metric="dotproduct",  # Similarity metric
        spec=spec
    )
    while not pc.describe_index(PINECONE_INDEX_NAME).status.ready:
        print("Waiting for index to be ready...")
        time.sleep(1)
    
index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))

#LOAD, SPLIT AND EMBED DOCUMENTS

def load_vectorstore(uploaded_files):
    embed_model = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    file_paths = []

    #1. Upload
    for file in uploaded_files:
        save_path = Path(UPLOAD_DIR) / file.filename
        with open(save_path, "wb") as f:
            f.write(file.file.read())
        file_paths.append(str(save_path))

    #2 Split
    for file_path in file_paths:
        loader=PyPDFLoader(file_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        chunks= splitter.split_documents(documents)

        texts = [chunk.page_content for chunk in chunks]
        metadata = [chunk.metadata for chunk in chunks]
        ids = [f"{Path(file_path).stem}-{i}" for i in range(len(chunks))]
    
    #3 Embedding
    print(f"Embedding chunks")
    embedding = embed_model.embed_documents(texts)

    #4Upsering the Embedding
    print("Userting Embeddings...")
    with tqdm(total=len(embedding),desc="Upserting to Pinecone") as progress:
        index.upsert(vectors=zip(ids,embedding,metadata))
        progress.update(len(embedding))

    print(f"Upload Complete for {file_path}")   