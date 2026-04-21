from langchain_community.document_loaders import PyPDFLoader
import os
from src.ingestion.text_cleaner import clean_text
from src.chunking.chunker import chunk_documents
from src.embeddings.embedder import embed_documents
from src.vectorstore.qdrant_client import (
    get_qdrant_client,
    create_collection,
    upload_embeddings
)
from src.retrieval.retriever import retrieve_documents
from src.generation.generator import generate_answer

DATA_PATH = "data/raw"

def load_all_pdfs(data_path):
    documents = []
    
    for file in os.listdir(data_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(data_path, file)
            print(f"\nLoading: {file}")
            
            loader = PyPDFLoader(file_path)
            docs = loader.load()
            
            print(f"Pages loaded: {len(docs)}")
            
            for doc in docs:
                doc.page_content = clean_text(doc.page_content)
                doc.metadata["source"] = file
            
            documents.extend(docs)
            
    return documents

if __name__ == "__main__":
    docs = load_all_pdfs(DATA_PATH)
    
    print("\nTotal documents (pages): ", len(docs))
    
    chunks = chunk_documents(docs)
    
    print(f"\nTotal chunks created: {len(chunks)}")
    
    # Inspect first few pages
    for i, chunk in enumerate(chunks[:3]):
        print(f"\n{'='*40}")
        print(f"Chunk {i+1}")
        print(f"Source: {chunk.metadata['source']}")
        print(f"{'='*40}\n")
        
        print(chunk.page_content[:1000])     # first 800 chars
        
    print("\nGenerate embeddings...")
    embeddings = embed_documents(chunks)
    
    print(f"Embeddings generated: {len(embeddings)}")
    
    client = get_qdrant_client()
    
    vector_size = len(embeddings[0]["vector"])
    collection_name = "manufacturing_docs"
    
    create_collection(client, collection_name, vector_size)
    
    upload_embeddings(client, collection_name, embeddings)
    
    print("\nData successfully stored in Qdrant!")
    
    query = "how to tighten conveyor belt"
    
    print("\nSearching...\n")
    
    results = retrieve_documents(client, collection_name, query)
    
    for i, res in enumerate(results):
        print(f"\nResult {i+1}")
        print(res.payload["text"][:500])
        
    # Combine retrieved chunks
    context = "\n\n".join([res.payload["text"][:300] for res in results])
    
    answer = generate_answer(query, context)
    
    print("\nFINAL ANSWER:\n")
    print(answer.strip())