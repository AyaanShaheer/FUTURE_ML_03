from flask import Flask, render_template, request
from retriever import FAQRetriever
from generator import RAGGenerator
from datetime import datetime
import csv

app = Flask(__name__)

# Initialize the retriever and generator
retriever = FAQRetriever("faq_data.csv")
generator = RAGGenerator()

# Logging function
def log_interaction(query, top_match, response):
    with open("chat_logs.csv", mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), query, top_match, response])

# Main chat route
@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_query = request.form["query"]
        docs = retriever.retrieve(user_query)
        response = generator.generate(user_query, docs)
        top_match = docs[0]['question'] if docs else "N/A"
        log_interaction(user_query, top_match, response)
    return render_template("index.html", response=response)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
