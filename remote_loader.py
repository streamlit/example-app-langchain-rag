import requests
import os

from langchain_community.document_loaders import WebBaseLoader, WikipediaLoader
from local_loader import get_document_text
from langchain_community.document_loaders import OnlinePDFLoader


# if you want it locally, you can use:
CONTENT_DIR = os.path.dirname(__file__)


# an alternative if you want it in /tmp or equivalent.
# CONTENT_DIR = tempfile.gettempdir()

def load_web_page(page_url):
    loader = WebBaseLoader(page_url)
    data = loader.load()
    return data


def load_online_pdf(pdf_url):
    loader = OnlinePDFLoader(pdf_url)
    data = loader.load()
    return data


def filename_from_url(url):
    filename = url.split("/")[-1]
    return filename


def download_file(url, filename=None):
    response = requests.get(url)
    if not filename:
        filename = filename_from_url(url)

    full_path = os.path.join(CONTENT_DIR, filename)

    with open(full_path, mode="wb") as f:
        f.write(response.content)
        download_path = os.path.realpath(f.name)
    print(f"Downloaded file {filename} to {download_path}")
    return download_path


def get_wiki_docs(query, load_max_docs=2):
    wiki_loader = WikipediaLoader(query=query, load_max_docs=load_max_docs)
    docs = wiki_loader.load()
    for d in docs:
        print(d.metadata["title"])
    return docs


def main():
    # run through the different remote loading functions.
    problems_of_philosophy_by_russell = "https://www.gutenberg.org/ebooks/5827.html.images"
    docs = load_web_page(problems_of_philosophy_by_russell)
    for doc in docs:
        print(doc)

    math_analysis_of_logic_by_boole = "https://www.gutenberg.org/files/36884/36884-pdf.pdf"
    local_pdf_path = download_file(math_analysis_of_logic_by_boole)

    with open(local_pdf_path, "rb") as pdf_file:
        docs = get_document_text(pdf_file, title="Analysis of Logic")

    for doc in docs:
        print(doc)

    problems_of_philosophy_pdf = "https://s3-us-west-2.amazonaws.com/pressbooks-samplefiles/LewisTheme/The-Problems-of-Philosophy-LewisTheme.pdf"
    docs = load_online_pdf(problems_of_philosophy_pdf)
    for doc in docs:
        print(doc)


if __name__ == "__main__":
    main()
