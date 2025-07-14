
# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get update && apt-get install -y wget unzip && \
    wget https://github.com/allure-framework/allure2/releases/download/2.24.1/allure-2.24.1.zip && \
    unzip allure-2.24.1.zip && mv allure-2.24.1 /opt/allure && ln -s /opt/allure/bin/allure /usr/bin/allure

# Run default command
CMD ["streamlit", "run", "streamlit_app.py"]
