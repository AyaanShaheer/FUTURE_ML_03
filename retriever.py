import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from text_preprocessing import preprocess_text

class FAQRetriever:
    def __init__(self, faq_path):
        self.df = pd.read_csv(faq_path)
        self.df['clean_question'] = self.df['question'].apply(preprocess_text)

        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['clean_question'])

        self.nn_model = NearestNeighbors(n_neighbors=3, metric='cosine')
        self.nn_model.fit(self.tfidf_matrix)

    def retrieve(self, user_query, k=3):
        clean_query = preprocess_text(user_query)
        query_vec = self.vectorizer.transform([clean_query])
        distances, indices = self.nn_model.kneighbors(query_vec, n_neighbors=k)

        results = []
        for i in indices[0]:
            results.append({
                'question': self.df.iloc[i]['question'],
                'answer': self.df.iloc[i]['answer']
            })
        return results
