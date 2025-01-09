# Use Python 3.9-slim image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install required tools and add MySQL repository
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    gnupg \
    lsb-release \
    && wget https://dev.mysql.com/get/mysql-apt-config_0.8.26-1_all.deb \
    && wget -qO - https://repo.mysql.com/RPM-GPG-KEY-mysql-2022 | gpg --dearmor -o /usr/share/keyrings/mysql.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/mysql.gpg] http://repo.mysql.com/apt/debian/ $(lsb_release -sc) mysql-8.0" > /etc/apt/sources.list.d/mysql.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends mysql-server \
    && rm -rf /var/lib/apt/lists/* /mysql-apt-config_0.8.26-1_all.deb

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
