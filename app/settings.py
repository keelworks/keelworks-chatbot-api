import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# CORS settings
ALLOWED_ORIGINS = os.getenv('ALLOWED_ORIGINS', "*").split(',')
#ALLOWED_ORIGINS = os.getenv('ALLOWED_ORIGINS', "http://localhost", "https://keelworks.org").split(',')
ALLOW_CREDENTIALS = os.getenv('ALLOW_CREDENTIALS', 'true').lower() == 'true'
ALLOW_METHODS = os.getenv('ALLOW_METHODS', '*').split(',')
ALLOW_HEADERS = os.getenv('ALLOW_HEADERS', '*').split(',')

# CORS middleware settings
def add_cors_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=ALLOW_CREDENTIALS,
        allow_methods=ALLOW_METHODS,
        allow_headers=ALLOW_HEADERS,
    )
