import re
from sentence_transformers import SentenceTransformer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Initialize model, stemmer, and lemmatizer
model = SentenceTransformer('all-MiniLM-L6-v2')
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Preprocess text (tokenization, stemming, lemmatization, and lowercasing)
def preprocess_text(text: str) -> str:
    text = re.sub(r'\W+', ' ', text)  # Remove non-alphanumeric characters
    text = text.lower()  # Convert to lowercase
    tokens = word_tokenize(text)  # Tokenize text
    tokens = [stemmer.stem(word) for word in tokens]  # Apply stemming
    tokens = [lemmatizer.lemmatize(word) for word in tokens]  # Apply lemmatization
    return ' '.join(tokens)  # Join tokens back into a single string

# Generate SBERT embeddings
def get_sbert_embedding(text: str) -> list[float]:
    embedding = model.encode(text)
    return embedding