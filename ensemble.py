import os
from dotenv import load_dotenv

from langchain_community.embeddings import HuggingFaceEmbeddings

from splitter import split_documents
from vector_store import create_vector_db

load_dotenv()


def ensemble_retriever_from_docs(docs, embeddings=None):
    texts = split_documents(docs)

    if embeddings is None:
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

    vs = create_vector_db(texts, embeddings)

    return vs.as_retriever(search_kwargs={"k": 4})
