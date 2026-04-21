import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.vectorstore.qdrant_client import get_qdrant_client
from src.retrieval.retriever import retrieve_documents
from src.generation.generator import generate_answer

st.title("🔧 Manufacturing Troubleshooting Assistant")

query = st.text_input("Enter you problem:")

if query:
    client = get_qdrant_client()
    collection_name = "manufacturing_docs"
    
    results = retrieve_documents(client, collection_name, query, top_k=2)
    context = "\n\n".join([res.payload["text"][:300] for res in results])
    
    answer = generate_answer(query, context)
    
    st.subheader("Solution:")
    st.write(answer)
    
    client.close()