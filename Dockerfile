# Use Ubuntu 20.04 as the base image
FROM ubuntu:20.04

# Set the working directory in the container
WORKDIR /app

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites and MySQL server
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    git \
    mysql-server \
    && rm -rf /var/lib/apt/lists/*

# Clone the FastAPI repository from GitHub
RUN git clone --depth 1 https://github.com/keelworks/keelworks-chatbot-api /app

# Install Python dependencies from the cloned repository
RUN pip3 install --no-cache-dir -r requirements.txt

# Generate chatbot model pickle file from root directory
RUN python3 -m scripts.save_model

# Expose the ports used by FastAPI and MySQL
EXPOSE 8000 3306

# Set MySQL root password and database name
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=""
ENV MYSQL_DATABASE=keelworks_chatbot_db

# Initialize MySQL and setup the database
RUN service mysql start && \
    mysql -u root -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY '${MYSQL_PASSWORD}';" && \
    mysql -u root -e "CREATE DATABASE ${MYSQL_DATABASE};"

# Command to start MySQL and run the FastAPI app
CMD ["sh", "-c", "service mysql start && sleep 5 && alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
