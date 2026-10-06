# Manufacturing Equipment Troubleshooting Assistant

A retrieval-augmented generation (RAG) application that helps technicians troubleshoot manufacturing equipment using information retrieved from industrial equipment manuals.

## Problem

Manufacturing troubleshooting often requires searching long technical manuals for the right procedure. This project turns that workflow into a semantic-search and grounded-answer pipeline.

## How It Works

```text
Industrial PDF Manuals
        |
        v
Text Extraction & Cleaning
        |
        v
Recursive Chunking
        |
        v
Sentence-Transformer Embeddings
        |
        v
Local Qdrant Vector Store
        |
        v
Top-K Semantic Retrieval
        |
        v
Ollama + TinyLlama
        |
        v
Grounded Troubleshooting Response
```

## Example

**Query**

> Conveyor belt is not moving

The system retrieves relevant sections from the indexed manuals and passes the retrieved context to a local LLM to produce a concise troubleshooting response.

## Key Features

- PDF ingestion for industrial equipment manuals
- Text cleaning and chunk filtering
- Recursive character-based chunking with overlap
- Sentence Transformer embeddings using `all-MiniLM-L6-v2`
- Persistent local Qdrant vector storage with cosine similarity
- Top-K semantic retrieval
- Grounded local LLM generation through Ollama
- Streamlit interface
- CLI query pipeline
- Separate ingestion, retrieval, vector-store, and generation modules

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| PDF processing | LangChain Community + PyPDF |
| Chunking | LangChain Text Splitters |
| Embeddings | Sentence Transformers |
| Vector database | Qdrant |
| LLM runtime | Ollama |
| Local model | TinyLlama |
| UI | Streamlit |

## Project Structure

```text
manufacturing-rag/
├── app/
│   └── streamlit_app.py
├── data/
│   └── raw/
│       └── *.pdf
├── src/
│   ├── ingestion/
│   ├── chunking/
│   ├── embeddings/
│   ├── vectorstore/
│   ├── retrieval/
│   ├── generation/
│   └── pipeline/
├── requirements.txt
└── README.md
```

## Run Locally

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Ollama and pull the local model

Install Ollama, then make sure the model used by the application is available:

```bash
ollama pull tinyllama
```

Keep the Ollama service running while querying the application.

### 4. Build the local vector index

Place the equipment manuals under `data/raw/`, then run:

```bash
python -m src.pipeline.ingest
```

This extracts and cleans the PDFs, creates chunks, generates embeddings, and stores them in the local Qdrant database under `data/qdrant_db/`.

### 5. Query from the CLI

```bash
python -m src.pipeline.query
```

Type a troubleshooting question and enter `exit` to stop.

### 6. Launch the Streamlit interface

```bash
streamlit run app/streamlit_app.py
```

## Engineering Notes

- The vector database runs locally using Qdrant's persistent local storage.
- Embeddings are generated locally with `all-MiniLM-L6-v2`.
- Answer generation uses Ollama, so no paid LLM API is required.
- The application is designed around document-grounded responses and instructs the local model to use only retrieved context.

## Limitations

- PDF extraction quality depends on the source manuals and can contain OCR or formatting noise.
- The quality of generated answers is constrained by the local language model.
- Retrieval is currently evaluated qualitatively rather than with a formal benchmark.
- The application currently uses a fixed collection name and retrieval depth.

## Future Improvements

- Metadata-aware retrieval and filtering
- Better OCR and document cleaning
- Retrieval evaluation with precision/recall or relevance metrics
- Conversation history
- Reranking for improved retrieval quality
- Stronger local or hosted LLMs
- Production deployment

## Author

**Subham Dey**
