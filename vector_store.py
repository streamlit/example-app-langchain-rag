
import os
from langchain_community.embeddings import HuggingFaceEmbeddings, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from local_loader import get_document_text
from remote_loader import download_file
from splitter import split_documents


# This happens all at once, not ideal for large datasets.
def create_vector_db(texts, embeddings=None, collection_name="chroma"):
    # Select embeddings
    if not embeddings:
        # To use HuggingFace embeddings instead:
        # embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY, model="text-embedding-3-small")

    # Create a vectorstore from documents
    # this will be a chroma collection with a default name.
    db = Chroma(collection_name=collection_name,
                embedding_function=embeddings,
                persist_directory=os.path.join("store/", collection_name))
    db.add_documents(texts)

    # db = Chroma.from_documents(texts, embeddings)
    return db


def find_similar(vs, query):
    docs = vs.similarity_search(query)
    return docs


def main():
    pdf_filename = "examples/mal_boole.pdf"

    if not os.path.exists(pdf_filename):
        math_analysis_of_logic_by_boole = "https://www.gutenberg.org/files/36884/36884-pdf.pdf"
        local_pdf_path = download_file(math_analysis_of_logic_by_boole, pdf_filename)
    else:
        local_pdf_path = pdf_filename

    print(f"PDF path is {local_pdf_path}")

    with open(local_pdf_path, "rb") as pdf_file:
        docs = get_document_text(pdf_file, title="Analysis of Logic")

    texts = split_documents(docs)
    vs = create_vector_db(texts)

    results = find_similar(vs, query="What is meant by the simple conversion of a proposition?")
    MAX_CHARS = 300
    print("=== Results ===")
    for i, text in enumerate(results):
        # cap to max length but split by words.
        content = text.page_content
        n = max(content.find(' ', MAX_CHARS), MAX_CHARS)
        content = text.page_content[:n]
        print(f"Result {i + 1}:\n {content}\n")


if __name__ == "__main__":
    main()
