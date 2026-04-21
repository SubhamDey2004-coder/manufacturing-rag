from src.vectorstore.qdrant_client import get_qdrant_client
from src.retrieval.retriever import retrieve_documents
from src.generation.generator import generate_answer

collection_name = "manufacturing_docs"

client = get_qdrant_client()

while True:
    query = input("\nEnter your query (or 'exit'): ")
    
    if query.lower() == "exit":
        break
    
    results = retrieve_documents(client, collection_name, query, top_k=2)
    
    context = "\n\n".join([res.payload["text"][:300] for res in results])
    
    answer = generate_answer(query, context)
    
    print("\nFINAL ANSWER:\n")
    print("\n" + answer.replace("Answer the question using ONLY the given context.", "").strip())
    
    client.close()