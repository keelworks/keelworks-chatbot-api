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

# Define model and embeddings to save
model_data = {
    'model': model,
    'faq_questions': faq_questions,
    'faq_embeddings': faq_embeddings,
    'faqs': faqs
}

# Define the directory and file name
model_directory = 'model'
file_name = 'chatbot_model.pkl'
file_path = os.path.join(model_directory, file_name)

# Save model_data as pickle file
with open(file_path, 'wb') as f:
    pickle.dump(model_data, f)

print(f"Model and embeddings saved to {file_path}")

# To run this script:
# python -m scripts.save_model