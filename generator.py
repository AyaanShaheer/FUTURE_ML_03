from transformers import T5Tokenizer, T5ForConditionalGeneration

class RAGGenerator:
    def __init__(self, model_name="google/flan-t5-small"):
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)

    def generate(self, user_query, retrieved_docs):
        context = "\n".join([f"Q: {item['question']} A: {item['answer']}" for item in retrieved_docs])
        prompt = f"Given the following FAQ context:\n{context}\n\nAnswer this question:\n{user_query}"

        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)
        output = self.model.generate(**inputs, max_new_tokens=100)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

