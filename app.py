import streamlit as st
import pickle
from preprocessing import transform_text

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Movie Review Sentiment Analysis")

user_input = st.text_area("Enter the review")

if st.button('Predict'):
    if not user_input.strip():
        st.warning("Please enter a review first.")
    else:
        transformed_review = transform_text(user_input)
        vector_input = tfidf.transform([transformed_review])
        result = model.predict(vector_input)[0]

        if result == 1:
            st.header("Positive")
        else:
            st.header("Negative")