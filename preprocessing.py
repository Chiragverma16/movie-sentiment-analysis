import nltk
import string
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

try:
    nltk.data.find('tokenizers/punkt')
except:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except:
    nltk.download('stopwords')

ps = PorterStemmer()
STOP_WORDS = set(stopwords.words('english'))

def transform_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', ' ', text)
    words = nltk.word_tokenize(text)
    words = [w for w in words if w.isalnum()]
    words = [w for w in words if w not in STOP_WORDS and w not in string.punctuation]
    words = [ps.stem(w) for w in words]
    return " ".join(words)