# 🩺 Modular RAG Medical AI Assistant

This assistant allows users to upload their own medical documents (PDFs), retrieve information from them using advanced RAG (Retrieval-Augmented Generation) techniques, and receive accurate, context-specific answers. The project is designed for production, featuring a modular architecture with separate services for the backend and frontend.

## ✨ Features

* **Document Upload & Embedding:** Users can upload multiple PDF documents.
* **Contextual Retrieval (RAG):** The chatbot answers questions based *only* on the content of the uploaded documents.
* **Modular Architecture:** Separate `server` (FastAPI) and `client` (Streamlit) directories.
* **Precise LLM Guidance:** Uses a custom prompt to instruct the LLM to provide factual, calm, and respectful answers, with an explicit rule to **never provide medical advice**.
* **Chat History:** Chat history is maintained and can be downloaded.
* **Full Deployment:** Includes steps and configurations for deploying both the backend and frontend.

## ⚙️ Technology Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend Framework** | **FastAPI** | High-performance API server. |
| **Frontend Framework** | **Streamlit** | Interactive web application UI. |
| **RAG/Orchestration** | **LangChain** | Managing the document processing and LLM chains. |
| **Large Language Model (LLM)** | **Groq Llama 3** (70B) | High-speed inference for generating responses. |
| **Embedding Model** | **Google GenAI \`embedding-001\`** | Creating vector representations of documents (768 dimensions). |
| **Vector Database** | **Pinecone** | Cloud-native vector storage, ideal for deployment. |
| **Deployment (Backend)** | **Render** | Hosting the production FastAPI service. |
| **Deployment (Frontend)** | **Streamlit Cloud** | Hosting the production Streamlit application. |
| **Dependencies** | **\`uv\` / \`pydantic\` / \`python-dotenv\`** | Package management, data validation, and environment configuration. |

## 🚀 Getting Started

Follow these steps to set up the project locally.

### 1. Prerequisites

You need the following API keys and accounts:

1.  **Groq API Key:** For the Llama 3 LLM.
2.  **Gemini API Key:** For Google's `embedding-001` model.
3.  **Pinecone API Key & Environment:** For the vector database.

### 2. Setup Environment

Clone the repository and create a virtual environment:

git clone (https://github.com/AnjaliDhosariya/Medical-AI-Assistant)
cd Medical-AI-Assistant

#### Assuming you have uv or venv/pip installed
uv venv
source .venv/bin/activate
### 3. Configure API Keys

Create an environment file named **\`.env\`** in the root directory and add your keys.

### 4. Install Dependencies

The project uses separate \`requirements.txt\` files for the server and client.

\`\`\`bash
# Install Server Dependencies (from the 'server' directory)
cd server
uv pip install -r requirements.txt
cd ..

# Install Client Dependencies (from the 'client' directory)
cd client
uv pip install -r requirements.txt
cd ..
\`\`\`

### 5. Run the Backend (Server)

Navigate to the \`server\` directory and start the FastAPI application:

\`\`\`bash
cd server
uvicorn main:app --reload
\`\`\`

The server will be live at \`http://127.0.0.1:8000\`.

### 6. Run the Frontend (Client)

In a separate terminal, navigate to the \`client\` directory and start the Streamlit application:

\`\`\`bash
cd client
streamlit run app.py
\`\`\`

The Streamlit app will open in your browser, ready for you to upload documents and begin asking questions!



## 🧑‍💻 File Structure

\`\`\`
├── client/                     # Frontend Streamlit Application
│   ├── components/             # UI Modules (Chat, Uploader, History)
│   ├── utils/                  # API communication functions
│   ├── config.py               # API_URL configuration
│   ├── app.py                  # Main Streamlit entry point
│   └── requirements.txt        # Streamlit dependencies
├── server/                     # Backend FastAPI Application
│   ├── modules/                # Core RAG logic (LLM, Vector Store, Handlers)
│   ├── routes/                 # API Endpoints (Upload & Ask)
│   ├── middleware/             # Exception Handlers
│   ├── main.py                 # FastAPI entry point
│   └── requirements.txt        # FastAPI dependencies
├── .env                        # Environment variables (IGNORED by Git)
├── .gitignore
└── README.md
\`\`\`
