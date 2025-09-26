from langchain.prompts import PromptTemplate 
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")

def get_llm_chain(retriever):
    llm=ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name='llama3-70b-8192',
        streaming=True,  # ✅ streaming enabled
        callbacks=[StreamingStdOutCallbackHandler()]
    )
    prompt=PromptTemplate(
        input_variables=["context","question"],
        template=""" 
        You are an AI-powered medical assistant trained to help users understant medical documents and health-related questions.

        Your job is to provide clear,accurate,and helpful responses based **only on the provided context**.
        
        ---

        **Context**:
        {context}
        **User Question**:
        {question}

        ---

        **Answer**:
        - Respond in a calm,factual and respectful tone.
        - Use simple explanations when needed.
        - If the context does not contain the answer, say: "I am sorry,but I could'nt find relevant
        information in the provided documents.
        - DO NOT makeup facts.
        - Do NOT give medical advice or diagnosis.
        """
    )
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt":prompt},
        return_source_documents=True
    )