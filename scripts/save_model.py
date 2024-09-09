import os
import json
import pickle
# import nltk
import numpy as np
from utils.preprocess_and_embeddings import model, preprocess_text, get_sbert_embedding

# # Get the path to the virtual environment's directory
# venv_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'venv')

# # Set the path for nltk_data inside the virtual environment's lib directory
# nltk_data_path = os.path.join(venv_dir, 'lib', 'python3.12', 'site-packages', 'nltk_data')

# # Ensure the directory exists
# os.makedirs(nltk_data_path, exist_ok=True)

# # Set NLTK_DATA environment variable to point to this directory
# os.environ['NLTK_DATA'] = nltk_data_path

# # Download the required NLTK data
# nltk.download('punkt', download_dir=os.environ['NLTK_DATA'])
# nltk.download('wordnet', download_dir=os.environ['NLTK_DATA'])
# nltk.download('omw-1.4', download_dir=os.environ['NLTK_DATA'])

# Load the FAQs from the JSON file
with open('data/faqs.json', 'r') as file:
    data = json.load(file)

faqs = data['faqs']

# Precompute embeddings for FAQ questions
faq_questions = [preprocess_text(faq['question']) for faq in faqs]
faq_embeddings = np.array([get_sbert_embedding(question) for question in faq_questions])

# Define chatbot_model and embeddings to save as pickle file
chatbot_model = {
    'model': model,
    'faqs': faqs,
    'faq_embeddings': faq_embeddings,
    'threshold': 0.5,
}

# Define the directory and file name
file_path = os.path.join('model', 'chatbot_model.pkl')

# Save model_data as pickle file
with open(file_path, 'wb') as f:
    pickle.dump(chatbot_model, f)

print(f'Model and embeddings saved to {file_path}')
