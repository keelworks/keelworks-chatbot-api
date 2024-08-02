import nltk
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from utils.preprocess_and_embeddings import preprocess_text, get_sbert_embedding

# Load NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Find the best matching answer
def get_best_answer(user_query, faqs, faq_embeddings, threshold=0.5):
    preprocessed_query = preprocess_text(user_query)
    query_embedding = get_sbert_embedding(preprocessed_query).reshape(1, -1)

    similarities = cosine_similarity(query_embedding, faq_embeddings)
    best_match_index = similarities.argmax()
    best_match_score = similarities[0, best_match_index]

    if best_match_score < threshold:
        return "Sorry, I don't have the answer. Please email to test@keelworks to get more info."
    
    return faqs[best_match_index]['answer']

# Load model and embeddings from pickle file
with open('model/chatbot_model.pkl', 'rb') as f:
    model_data = pickle.load(f)

model = model_data['model']
faqs = model_data['faqs']
faq_questions = model_data['faq_questions']
faq_embeddings = model_data['faq_embeddings']