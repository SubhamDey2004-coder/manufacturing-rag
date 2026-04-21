from src.ingestion.pdf_loader import load_all_pdfs
from src.chunking.chunker import chunk_documents
from src.embeddings.embedder import embed_documents
from src.vectorstore.qdrant_client import (
    get_qdrant_client,
    create_collection,
    upload_embeddings
)

DATA_PATH = "data/raw"
collection_name = "manufacturing_docs"

if __name__ == "__main__":
    docs = load_all_pdfs(DATA_PATH)
    
    chunks = chunk_documents(docs)
    
    print(f"Total chunks: {len(chunks)}")
    
    embeddings = embed_documents(chunks)
    
    client = get_qdrant_client()
    
    vector_size = len(embeddings[0]["vector"])
    
    create_collection(client, collection_name, vector_size)
    upload_embeddings(client, collection_name, embeddings)
    
    print("\nData stored permanentky in Qdrant!")
    
    client.close()