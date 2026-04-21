from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

def get_qdrant_client():
    return QdrantClient(path="data/qdrant_db")    # local in-memory for now

def create_collection(client, collection_name, vector_size):
    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=vector_size,
            distance=Distance.COSINE
        )
    )
    
def upload_embeddings(client, collection_name, embeddings):
    points = [
        PointStruct(
            id=idx,
            vector=item["vector"],
            payload=item["payload"]
        )
        for idx, item in enumerate(embeddings)
    ]
    
    client.upsert(
        collection_name=collection_name,
        points=points
    )