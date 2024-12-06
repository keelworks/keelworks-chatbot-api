# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install git so we can clone the repo
RUN apt-get update && apt-get install -y git

# Clone the FastAPI repository from GitHub
RUN git clone https://github.com/jjpark987/keelworks-chatbot-api.git /app

# Install Python dependencies from the cloned repository
RUN pip install --no-cache-dir -r requirements.txt

# Generate chatbot model pickle file from root directory
RUN python -m scripts.save_model

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
