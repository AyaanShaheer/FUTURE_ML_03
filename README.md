
```markdown
# 🤖 FUTURE_ML_03 – Customer Support RAG Chatbot

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-lightgrey)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project is **Task 3** for the FUTURE Machine Learning Internship.

It is a **Retrieval-Augmented Generation (RAG)**-based customer support chatbot capable of answering queries using a combination of:

- 🔍 **TF-IDF + Nearest Neighbors** for document retrieval
- 🧠 **Hugging Face flan-T5-small** for natural response generation
- 💬 **Flask UI** for user interaction
- 📊 **Streamlit dashboard** for chat insights

---

## 🚀 Features

✅ RAG Pipeline (Retriever + Generator)  
✅ NLP preprocessing with NLTK  
✅ Clean & responsive web-based chat UI  
✅ Interaction logging and analytics  
✅ Streamlit dashboard with insights  
✅ Modular and extensible codebase  

---

## 🛠️ Tech Stack

- **Python 3.10**
- **NLTK**, **scikit-learn** for preprocessing + retrieval
- **Transformers** for flan-T5 generator
- **Flask** for chatbot interface
- **Streamlit** for dashboard

---

## 📁 Project Structure

```

FUTURE\_ML\_03/
├── app.py                  # Flask app for chatbot
├── generator.py            # Hugging Face-based generator
├── retriever.py            # TF-IDF vector retriever
├── text\_preprocessing.py   # Preprocessing utility
├── dashboard\_app.py        # Streamlit insights dashboard
├── faq\_data.csv            # Sample support FAQ data
├── chat\_logs.csv           # Logs user queries and bot responses
├── templates/
│   └── index.html          # Chat UI (Flask template)
└── README.md               # You are here!

````

---

## 🧪 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/AyaanShaheer/FUTURE_ML_03.git
cd FUTURE_ML_03
````

### 2. Set up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Chatbot App

```bash
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 📊 Analytics Dashboard

To view chat logs and top FAQs:

```bash
streamlit run dashboard_app.py
```

---

## 📸 Screenshots

### 💬 Chat UI

![Screenshot 2025-06-19 165618](https://github.com/user-attachments/assets/bd563fb6-7160-4682-bf1d-1cbf1f6c65de)

![Screenshot 2025-06-19 165551](https://github.com/user-attachments/assets/0c2c48cd-9143-432d-baf7-ed2388ccadb3)

![Screenshot 2025-06-19 165712](https://github.com/user-attachments/assets/3cf4d412-60e1-44e6-aa1a-87965331e8cd)

![Screenshot 2025-06-19 165720](https://github.com/user-attachments/assets/12becfaa-5cb0-48ca-aa60-901a2a6950f5)

---


## 📚 Learnings

* RAG-based NLP architecture
* Transformer-based generation with T5
* Practical chatbot deployment with Flask
* Streamlit for data visualization
* Clean UI/UX design

---

## 🙌 Author

**Ayaan Shaheer**
Connect on [LinkedIn]((https://linkedin.com/in/ayaan-shaheer-74a087230))
GitHub: [@AyaanShaheer](https://github.com/AyaanShaheer)
Portfolio Website: [Portfolio](https://chatprofolio.vercel.app/profile/ayaanshaheer)

---

## 📜 License

MIT License — use freely with attribution.
