# 🔧 Manufacturing Equipment Troubleshooting Assistant (RAG System)

## 📌 Project Overview

This project is a **Retrieval-Augmented Generation (RAG) system** designed to assist technicians in diagnosing and troubleshooting manufacturing equipment issues.

Given a user query (e.g., *"conveyor belt not moving"*), the system:

1. Retrieves relevant sections from machinery manuals
2. Generates a structured troubleshooting response

---

## 🎯 Objective

To build an intelligent assistant that:

* Understands technical queries
* Retrieves accurate information from manuals
* Provides step-by-step troubleshooting guidance

---

## 🧠 System Architecture

```
PDF Manuals → Text Cleaning → Chunking → Embeddings → Qdrant Vector DB
                                                      ↓
                                                      Retrieval (Top-K)
                                                      ↓
                                                      LLM (Ollama)
                                                      ↓
                                                      Generated Answer
```

---

## 📂 Project Structure

```
manufacturing-rag/
│
├── data/
│   ├── raw/                  # PDF manuals
│   └── qdrant_db/            # Local vector database (persistent)
│
├── src/
│   ├── ingestion/            # PDF loading & cleaning
│   ├── chunking/             # Text chunking logic
│   ├── embeddings/           # Embedding generation
│   ├── vectorstore/          # Qdrant setup & upload
│   ├── retrieval/            # Document retrieval
│   └── generation/           # Answer generation (LLM)
│
├── app/
│   └── streamlit_app.py      # UI interface
│
├── src/pipeline/
│   ├── ingest.py             # One-time data ingestion
│   └── query.py              # Interactive query system
│
└── README.md
```

---

## ⚙️ Technologies Used

* **LangChain** – Document loading & processing
* **SentenceTransformers** – Embeddings (`all-MiniLM-L6-v2`)
* **Qdrant** – Vector database (local persistent storage)
* **Ollama** – Local LLM (TinyLlama / Phi3)
* **Streamlit** – User Interface

---

## 🚀 Features Implemented

* ✅ PDF ingestion from real industrial manuals
* ✅ Text cleaning and preprocessing
* ✅ Smart chunking for technical documents
* ✅ Embedding generation (local, no API cost)
* ✅ Persistent vector storage using Qdrant
* ✅ Semantic search (Top-K retrieval)
* ✅ Context-based answer generation
* ✅ Dynamic query input (no hardcoding)
* ✅ Streamlit UI for interaction

---

## 🧪 Example Query

```
Input:
"conveyor belt not moving"

Output:
- Relevant manual section retrieved
- Step-by-step troubleshooting instructions generated
```

---

## ▶️ How to Run

### 1. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Ingestion (Only Once)

```
python -m src.pipeline.ingest
```

### 4. Run Query System (CLI)

```
python -m src.pipeline.query
```

### 5. Run Streamlit UI

```
streamlit run app/streamlit_app.py
```

---

## 📊 Current Status

* ✔ Fully functional RAG pipeline
* ✔ Local vector database (persistent)
* ✔ Real-time query processing
* ✔ Working UI interface

---

## ⚠️ Limitations

* OCR noise in PDF text (minor spelling inconsistencies)
* Output formatting can be improved
* Small local models may limit response quality

---

## 🔮 Future Improvements

* Improve text cleaning and normalization
* Use stronger LLM (for better reasoning)
* Add chat history in UI
* Metadata-based filtering (e.g., troubleshooting sections only)
* Deploy as a web application

---

## 🙌 Conclusion

This project demonstrates a complete end-to-end **RAG system** using real-world industrial manuals. It showcases how AI can assist in practical problem-solving in manufacturing environments.

---
