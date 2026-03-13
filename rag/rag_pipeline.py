from models.llm import get_chatgroq_model
from rag.retriever import get_retriever

def generate_answer(question):

    model = get_chatgroq_model()

    retriever = get_retriever()

    docs = retriever.get_relevant_documents(question)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}
"""

    response = model.invoke(prompt)

    return response.content