from langchain.retrievers.document_compressors import DocumentCompressorPipeline
from langchain_community.document_transformers import EmbeddingsRedundantFilter, LongContextReorder
from langchain_community.embeddings import HuggingFaceBgeEmbeddings, HuggingFaceEmbeddings
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever, ContextualCompressionRetriever, MergerRetriever
from langchain.chains import RetrievalQA

from basic_chain import get_model
from remote_loader import load_web_page
from splitter import split_documents
from vector_store import create_vector_db

from dotenv import load_dotenv


def create_retriever(texts):
    dense_embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    sparse_embeddings = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-large-en",
                                                 encode_kwargs={'normalize_embeddings': False})
    dense_vs = create_vector_db(texts, collection_name="dense", embeddings=dense_embeddings)
    sparse_vs = create_vector_db(texts, collection_name="sparse", embeddings=sparse_embeddings)
    vector_stores = [dense_vs, sparse_vs]

    emb_filter = EmbeddingsRedundantFilter(embeddings=sparse_embeddings)
    reordering = LongContextReorder()
    pipeline = DocumentCompressorPipeline(transformers=[emb_filter, reordering])

    base_retrievers = [vs.as_retriever() for vs in vector_stores]
    lotr = MergerRetriever(retrievers=base_retrievers)

    compression_retriever_reordered = ContextualCompressionRetriever(
        base_compressor=pipeline, base_retriever=lotr, search_kwargs={"k": 5, "include_metadata": True}
    )
    return compression_retriever_reordered


def ensemble_retriever_from_docs(docs):
    texts = split_documents(docs)
    vs_retriever = create_retriever(texts)

    bm25_retriever = BM25Retriever.from_texts([t.page_content for t in texts])

    ensemble_retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, vs_retriever], weights=[0.5, 0.5])

    return ensemble_retriever


def main():
    load_dotenv()

    problems_of_philosophy_by_russell = "https://www.gutenberg.org/ebooks/5827.html.images"

    docs = load_web_page(problems_of_philosophy_by_russell)
    ensemble_retriever = ensemble_retriever_from_docs(docs)
    llm = get_model()
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=ensemble_retriever)

    results = qa.invoke("What are the key problems of philosophy according to Russell?")
    print(results)


if __name__ == "__main__":
    main()
