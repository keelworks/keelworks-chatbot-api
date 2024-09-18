# KeelWorks Chatbot API

This repository contains the backend code for the KeelWorks chatbot built with FastAPI. It handles user queries and provide answers based on a machine learning model, which is loaded from a pickle file. The API interacts with a MySQL database to store unanswered questions.

## Getting Started

### Prerequisites

- Python 3.10+
- MySQL server

### Installation

1. Clone the repository

```zsh
git clone git@github.com:jjpark987/Entity-Extraction-Chatbot-API.git
```

2. Create a virtual environment

```zsh
python -m venv .venv
```

3. Activate virtual environment

```zsh
source .venv/bin/activate
```

4. Install dependencies

```zsh
pip install -r requirements.txt
```

5. Generate chatbot model pickle file from root directory

```zsh
python -m scripts.save_model
```

6. Run API server

```zsh
uvicorn app.main:app --host 0.0.0.0 --port 80
```

The API should now be running at http://0.0.0.0:80.

## API Endpoints

- GET '/': Fetches the initial message from API.
- POST '/ask': Sends the user's question and receives the response from chatbot model.

## Contact

For any questions or issues, please reach out to jason.park@keelworks.org.
