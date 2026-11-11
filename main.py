from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about a coffee shop.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def format_reviews(docs):
    formatted = []
    for doc in docs:
        rating = doc.metadata.get("rating", "N/A")

        formatted.append(f"Rating: {rating}/5\nReview: {doc.page_content}")

    return "\n\n---\n\n".join(formatted)

while True:
    print("\n\n------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question.lower() == "q":
        break

    raw_reviews = retriever.invoke(question)
    formatted_reviews = format_reviews(raw_reviews)

    result = chain.invoke({"reviews": formatted_reviews, "question": question})
    print(result)