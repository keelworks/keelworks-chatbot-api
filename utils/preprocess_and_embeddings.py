import os
import re
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sentence_transformers import SentenceTransformer

# Set the NLTK data path to your virtual environment's lib directory
nltk_data_path = os.path.join(os.path.dirname(__file__), '..', '.venv', 'lib', 'python3.12', 'site-packages', 'nltk_data')
nltk.data.path.append(nltk_data_path)

# Set NLTK_DATA environment variable to point to this directory
os.environ['NLTK_DATA'] = nltk_data_path

# Ensure required NLTK resources are downloaded
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab', download_dir=os.environ['NLTK_DATA'])

try:
    nltk.data.find('wordnet')
except LookupError:
    nltk.download('wordnet', download_dir=os.environ['NLTK_DATA'])

try:
    nltk.data.find('omw-1.4')
except LookupError:
    nltk.download('omw-1.4', download_dir=os.environ['NLTK_DATA'])

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
