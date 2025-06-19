import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

st.set_page_config(page_title="Chatbot Insights", layout="wide")

# Load chat logs
def load_data():
    df = pd.read_csv("chat_logs.csv", names=["timestamp", "query", "top_match", "response"], parse_dates=["timestamp"])
    return df

# Load data
df = load_data()

st.title("📊 Chatbot Insights Dashboard")

if df.empty:
    st.warning("No data logged yet. Interact with the chatbot to populate data.")
else:
    # Top user queries
    st.subheader("🔁 Most Frequent User Queries")
    top_queries = df['query'].value_counts().head(5)
    st.bar_chart(top_queries)

    # Top matched FAQs
    st.subheader("📌 Most Retrieved FAQs")
    top_faqs = df['top_match'].value_counts().head(5)
    st.bar_chart(top_faqs)

    # Display full log
    st.subheader("📋 Full Interaction Log")
    st.dataframe(df.tail(20).sort_values("timestamp", ascending=False))
