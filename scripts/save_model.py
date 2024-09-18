import os
import json
import pickle
import numpy as np
from utils.preprocess_and_embeddings import model, preprocess_text, get_sbert_embedding

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
