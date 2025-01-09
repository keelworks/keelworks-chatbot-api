# Use Ubunti 20.04
FROM ubuntu:20.04

# Set the working directory in the container
WORKDIR /app

# Install required tools and add MySQL repository
RUN apt-get update && apt-get install -y wget gnupg && \
    wget https://dev.mysql.com/get/mysql-apt-config_0.8.26-1_all.deb && \
    dpkg -i mysql-apt-config_0.8.26-1_all.deb && \
    apt-get update && \
    apt-get install -y mysql-server && \
    rm -rf /var/lib/apt/lists/*

# Clone the FastAPI repository from GitHub
RUN apt-get install -y --no-install-recommends git && \
    git clone https://github.com/keelworks/keelworks-chatbot-api /app

# Install Python dependencies from the cloned repository
RUN pip install --no-cache-dir -r requirements.txt

# Generate chatbot model pickle file from root directory
RUN python -m scripts.save_model

# Expose the ports used by FastAPI and MySQL
EXPOSE 8000 3306

# Initialize MySQL and setup the database
RUN service mysql start && \
    mysql -e "CREATE DATABASE keelworks_chatbot_db;"

# Command to start MySQL and run the FastAPI app
CMD ["sh", "-c", "service mysql start && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
