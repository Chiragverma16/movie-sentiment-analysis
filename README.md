# 🎬 Movie Sentiment Analysis

A Natural Language Processing (NLP) web application that classifies movie reviews as **Positive** or **Negative** using Machine Learning. Built with Scikit-learn and deployed using Streamlit.

## 🚀 Live Demo
[Click here to view the app](https://movie-sentiment-analysis-nlp.streamlit.app)

---

## 📌 Features
- Real-time sentiment prediction on movie reviews
- Text preprocessing pipeline with tokenization, stopword removal and stemming
- TF-IDF vectorization for feature extraction
- Hyperparameter tuning using Optuna for best model selection
- Clean and interactive UI built with Streamlit

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| NLP | NLTK |
| Machine Learning | Scikit-learn |
| Hyperparameter Tuning | Optuna |
| Web App | Streamlit |
| Model Serialization | Pickle |

---

## 📁 Project Structure
```
movie-sentiment-analysis/
│
├── preprocessing.py    # Text preprocessing and transformation pipeline
├── app.py              # Streamlit web application
├── vectorizer.pkl      # Saved TF-IDF vectorizer
├── model.pkl           # Saved trained ML model
├── notebook.ipynb      # EDA, model training and Optuna hyperparameter tuning
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## ⚙️ HOW IT WORKS

1. **Input** — User enters a movie review in the text box
2. **Preprocessing** — Text is cleaned, tokenized, stopwords are removed and stemming is applied
3. **Vectorization** — Preprocessed text is converted to numerical features using TF-IDF
4. **Prediction** — Trained ML model predicts the sentiment
5. **Output** — Result is displayed as ✅ Positive or ❌ Negative

---

## 🧪 SAMPLE INPUTS

**Positive Reviews:**
> This movie was absolutely brilliant! The performances were incredible and the storyline was gripping.

> Amazing film with a heartwarming story. Loved every minute of it.

**Negative Reviews:**
> Horrible movie. The plot made no sense and the acting was terrible.

> Complete waste of time. Worst film I have seen in years.

---

## 🔧 RUN LOCALLY

**1. Clone the repository**
```bash
git clone https://github.com/Chiragverma16/movie-sentiment-analysis.git
cd movie-sentiment-analysis
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
python -m streamlit run app.py
```

---

## 📊 Model Training

- Multiple classifiers were evaluated including **Logistic Regression**, **Linear SVC** and **Multinomial Naive Bayes**
- **Optuna** was used for automated hyperparameter tuning across all classifiers
- Best performing model was saved as `model.pkl` for deployment
- Full training pipeline is available in `notebook.ipynb`
