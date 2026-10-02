from llm.chat import chat
from retrieval.retriever import retrive

def ask(question: str):
    chunks = retrive(question)

    context = "\n\n".join(
        chunk['text']
        for chunk in chunks
    )

    answer = chat(
        question=question,
        context=context
    )

    sources = [
        {
            "text":chunk['text']

        }
        for chunk in chunks
    ]

    return {
        "answer": answer,
        "sources": sources,
    }