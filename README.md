# KeelWorks Chatbot API

This is a FastAPI-based API for the KeelBot chatbot, designed to handle user queries and provide answers based on a machine learning model. The API interacts with a MySQL database to store unanswered questions.

## Getting Started

### Prerequisites

- Python 3.10+
- FastAPI
- SQLAlchemy
- MySQL server
- A working pickle file for the chatbot model (see below for instructions on generating it)

### Installation

1. Clone the repository

```zsh
git clone git@github.com:jjpark987/Entity-Extraction-Chatbot-API.git
```

2. Install dependencies

```zsh
pip install -r requirements.txt
```

3. Generate chatbot model pickle file from root directory

```zsh
python -m scripts.save_model
```

4. Run server

```zsh
uvicorn app.main:app --host 0.0.0.0 --port 80
```

The API should now be running at http://0.0.0.0:80.

## API Endpoints

- GET '/': Fetches the initial message from API
- POST '/ask': Sends the user's question and receives the response from chatbot model

## Contact

For any questions or issues, please reach out to jason.park@keelworks.org
