import pickle
from typing import Tuple
from sklearn.metrics.pairwise import cosine_similarity
from utils.preprocess_and_embeddings import preprocess_text, get_sbert_embedding

# Load chatbot model and embeddings from pickle file
with open('model/chatbot_model.pkl', 'rb') as f:
    chatbot_model = pickle.load(f)

model = chatbot_model['model']
faqs = chatbot_model['faqs']
faq_embeddings = chatbot_model['faq_embeddings']
threshold = chatbot_model['threshold']

# Find best matching answer using cosine_similarity and query embeddings
def get_best_answer(user_query: str) -> Tuple[str, bool]:
    preprocessed_query = preprocess_text(user_query)
    query_embedding = get_sbert_embedding(preprocessed_query).reshape(1, -1)

    similarities = cosine_similarity(query_embedding, faq_embeddings)
    best_match_index = similarities.argmax()
    best_match_score = similarities[0, best_match_index]
    is_above_threshold = best_match_score >= threshold
    
    return faqs[best_match_index]['answer'], is_above_threshold