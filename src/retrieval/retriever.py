from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_query_embedding(query):
    return model.encode(query).tolist()

def retrieve_documents(client, collection_name, query, top_k=2):
    query_vector = get_query_embedding(query)
    
    results = client.query_points(
        collection_name=collection_name,
        query=query_vector,
        limit=top_k
    )
    
    return results.points