# Use Python 3.9-slim image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install git so we can clone the repo
RUN apt-get update && apt-get install -y git \
    wget \
    gnupg \
    lsb-release \
    && wget https://dev.mysql.com/get/mysql-apt-config_0.8.26-1_all.deb \
    && dpkg -i mysql-apt-config_0.8.26-1_all.deb \
    && apt-get update \
    && apt-get install -y --no-install-recommends mysql-server \
    && rm -rf /var/lib/apt/lists/* /mysql-apt-config_0.8.26-1_all.deb

# Clone the FastAPI repository from GitHub
RUN git clone https://github.com/keelworks/keelworks-chatbot-api /app

# Install Python dependencies from the cloned repository
RUN pip install --no-cache-dir -r requirements.txt

# Generate chatbot model pickle file from root directory
RUN python -m scripts.save_model

# Expose the port that FastAPI will run on
EXPOSE 8000 3306

# Initialize MYSQL and setup the database
RUN service mysql start && \
    mysql -u root -e "CREATE DATABASE keelworks_chatbot_db;"

# Command to run the FastAPI app with Uvicorn
CMD service mysql start && \
    uvicorn app.main:app --host 0.0.0.0 --port 8000
