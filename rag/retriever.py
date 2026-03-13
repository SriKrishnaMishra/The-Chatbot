from langchain.vectorstores import Chroma
from models.embeddings import get_embeddings
from config.settings import VECTOR_DB_PATH

def get_retriever():

    embeddings = get_embeddings()

    vectordb = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever