import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from src.generation.generator import generate_answer
from src.retrieval.retriever import retrieve_documents
from src.vectorstore.qdrant_client import get_qdrant_client


COLLECTION_NAME = "manufacturing_docs"

st.title("🔧 Manufacturing Troubleshooting Assistant")
st.caption("Ask a troubleshooting question and get an answer grounded in the indexed equipment manuals.")

query = st.text_input("Describe the problem:")

if query.strip():
    client = get_qdrant_client()

    try:
        results = retrieve_documents(
            client,
            COLLECTION_NAME,
            query.strip(),
            top_k=2,
        )

        if not results:
            st.warning("No relevant manual sections were retrieved.")
        else:
            context = "\n\n".join(
                result.payload.get("text", "")[:500]
                for result in results
            )

            answer = generate_answer(query.strip(), context)

            st.subheader("Troubleshooting guidance")
            st.write(answer)
    except Exception as exc:
        st.error(f"Unable to process the request: {exc}")
    finally:
        client.close()
