from src.generation.generator import generate_answer
from src.retrieval.retriever import retrieve_documents
from src.vectorstore.qdrant_client import get_qdrant_client


COLLECTION_NAME = "manufacturing_docs"


def main():
    client = get_qdrant_client()

    try:
        while True:
            query = input("\nEnter your query (or 'exit'): ").strip()

            if query.lower() == "exit":
                break

            if not query:
                continue

            results = retrieve_documents(
                client,
                COLLECTION_NAME,
                query,
                top_k=2,
            )

            if not results:
                print("\nNo relevant manual sections were retrieved.")
                continue

            context = "\n\n".join(
                result.payload.get("text", "")[:500]
                for result in results
            )

            answer = generate_answer(query, context)

            print("\nFINAL ANSWER:\n")
            print(answer.strip())
    finally:
        client.close()


if __name__ == "__main__":
    main()
