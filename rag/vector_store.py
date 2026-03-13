from langchain.vectorstores import Chroma
from models.embeddings import get_embeddings
from config.settings import VECTOR_DB_PATH

def create_vector_store(chunks):

    embeddings = get_embeddings()

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    vectordb.persist()

    return vectordb