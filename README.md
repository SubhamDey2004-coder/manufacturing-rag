# Manufacturing Equipment Troubleshooting Assistant

A retrieval-augmented generation (RAG) application that helps technicians troubleshoot manufacturing equipment using information retrieved from industrial equipment manuals.

## Problem

Manufacturing troubleshooting often requires searching long technical manuals for the right procedure. This project turns that workflow into a semantic search and grounded-answer pipeline.

## How It Works

```text
Industrial PDF Manuals
        ↓
Text Extraction & Cleaning
        ↓
Chunking
        ↓
Sentence-Transformer Embeddings
        ↓
Qdrant Vector Database
        ↓
Top-K Semantic Retrieval
        ↓
Local LLM (Ollama)
        ↓
Grounded Troubleshooting Response
```

## Example

**Query**

> Conveyor belt is not moving

The system retrieves relevant manual sections and uses the retrieved context to generate a structured troubleshooting response.

## Key Features

- PDF ingestion for industrial manuals
- Text cleaning and document chunking
- Local embedding generation with Sentence Transformers
- Persistent vector storage with Qdrant
- Top-K semantic retrieval
- Local LLM inference with Ollama
- Streamlit interface
- CLI query pipeline
- Separation of ingestion, retrieval, and generation components

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Document processing | LangChain |
| Embeddings | Sentence Transformers |
| Vector database | Qdrant |
| LLM runtime | Ollama |
| UI | Streamlit |

## Project Structure

```text
manufacturing-rag/
├── app/
│   └── streamlit_app.py
├── config/
├── data/
├── src/
│   ├── ingestion/
│   ├── chunking/
│   ├── embeddings/
│   ├── vectorstore/
│   ├── retrieval/
│   ├── generation/
│   └── pipeline/
├── utils/
├── requirements.txt
└── README.md
```

## Run Locally

### 1. Create an environment

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Ingest the manuals

```bash
python -m src.pipeline.ingest
```

### 4. Run the query pipeline

```bash
python -m src.pipeline.query
```

### 5. Launch the UI

```bash
streamlit run app/streamlit_app.py
```

## Engineering Notes

The project uses local models and a local vector database, so the complete RAG pipeline can run without a paid LLM API.

Current limitations include OCR noise in some PDF content and the response-quality constraints of small local language models.

## Future Improvements

- Metadata-aware retrieval and filtering
- Better document cleaning/OCR handling
- Retrieval evaluation and relevance metrics
- Conversation history
- Stronger local or hosted LLMs
- Production deployment

## Author

**Subham Dey**
