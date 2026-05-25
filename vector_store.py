from langchain_community.vectorstores import Chroma


def create_vector_db(texts, embeddings):
    vector_db = Chroma.from_documents(
        documents=texts,
        embedding=embeddings
    )

    return vector_db
