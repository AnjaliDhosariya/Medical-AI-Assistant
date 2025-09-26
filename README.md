# 🩺 Modular RAG Medical AI Assistant

A production-ready **Retrieval-Augmented Generation (RAG) Medical Assistant** that enables users to upload medical documents (PDFs), retrieve context-specific information, and receive **factual, respectful, and safe answers**. The system follows a **modular architecture**, separating backend (FastAPI) and frontend (Streamlit).

⚠️ **Disclaimer:** This assistant is strictly informational and is explicitly instructed to **never provide medical advice**.

---

## ✨ Features

* **📄 Document Upload & Embedding** – Upload multiple PDF documents for analysis.
* **🔍 Contextual Retrieval (RAG)** – Answers questions *only* from uploaded documents.
* **🧩 Modular Architecture** – Separate `server` (FastAPI) and `client` (Streamlit) for maintainability.
* **🤖 Precise LLM Guidance** – Custom prompt ensures answers are factual, calm, and safe.
* **💬 Chat History** – Chat history is stored and downloadable.
* **🚀 Deployment Ready** – Separate configurations for deploying backend and frontend.

---

## ⚙️ Technology Stack

| Component                 | Technology                   | Purpose                              |
| ------------------------- | ---------------------------- | ------------------------------------ |
| **Backend Framework**     | FastAPI                      | High-performance API server          |
| **Frontend Framework**    | Streamlit                    | Interactive web UI                   |
| **RAG / Orchestration**   | LangChain                    | Document processing & LLM chaining   |
| **LLM**                   | Groq Llama 3 (70B)           | Fast, large-scale text generation    |
| **Embedding Model**       | Google GenAI `embedding-001` | Vector embeddings (768-dim)          |
| **Vector Database**       | Pinecone                     | Cloud-native vector storage          |
| **Deployment (Backend)**  | Render                       | Hosting FastAPI backend              |
| **Deployment (Frontend)** | Streamlit Cloud              | Hosting Streamlit frontend           |
| **Dependencies**          | uv, pydantic, python-dotenv  | Package mgmt, validation, env config |

---

## 🚀 Getting Started

### 1. Prerequisites

You’ll need the following API keys:

* **Groq API Key** – for Llama 3 model
* **Gemini API Key** – for Google embeddings
* **Pinecone API Key & Environment** – for vector DB

---

### 2. Clone & Setup

```bash
git clone https://github.com/AnjaliDhosariya/Medical-AI-Assistant
cd Medical-AI-Assistant

# Create and activate virtual environment
uv venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
```

---

### 3. Configure Environment

Create a `.env` file in the project root and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_env
```

---

### 4. Install Dependencies

The project uses separate requirements for server and client.

```bash
# Install backend (server) dependencies
cd server
uv pip install -r requirements.txt
cd ..

# Install frontend (client) dependencies
cd client
uv pip install -r requirements.txt
cd ..
```

---

### 5. Run the Backend

```bash
cd server
uvicorn main:app --reload
```

Backend will run at: `http://127.0.0.1:8000`

---

### 6. Run the Frontend

```bash
cd client
streamlit run app.py
```

Frontend will open in your browser.

---

## 🧑‍💻 File Structure

```
Medical-AI-Assistant/
├── client/                     # Frontend (Streamlit)
│   ├── components/             # UI modules (Chat, Uploader, History)
│   ├── utils/                  # API communication helpers
│   ├── config.py               # API_URL configuration
│   ├── app.py                  # Streamlit entry point
│   └── requirements.txt        # Dependencies for frontend
│
├── server/                     # Backend (FastAPI)
│   ├── modules/                # Core RAG logic (LLM, Vector store, Handlers)
│   ├── routes/                 # API endpoints (Upload, Ask)
│   ├── middleware/             # Exception handlers
│   ├── main.py                 # FastAPI entry point
│   └── requirements.txt        # Dependencies for backend
│
├── .env                        # API keys & config (ignored by Git)
├── .gitignore                  # Git ignore file
└── README.md                   # Project documentation
```

---

✅ With this setup, you can upload medical PDFs, query them, and get **factual, context-specific responses** saf
