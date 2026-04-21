from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    embedding = model.encode(text)
    return embedding.tolist()


def embed_documents(chunks):
    embeddings = []

    for chunk in chunks:
        emb = get_embedding(chunk.page_content)

        embeddings.append({
            "vector": emb,
            "payload": {
                "text": chunk.page_content,
                "source": chunk.metadata.get("source", "")
            }
        })

    return embeddings