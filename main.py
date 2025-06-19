from retriever import FAQRetriever
from generator import RAGGenerator

retriever = FAQRetriever("faq_data.csv")
generator = RAGGenerator()

query = "How do I update my shipping info?"
docs = retriever.retrieve(query)
response = generator.generate(query, docs)

print("🤖 Chatbot Response:")
print(response)
