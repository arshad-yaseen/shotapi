# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Run Python in unbuffered mode, for more real-time logs
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    curl \
    && curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb \
    && dpkg -i chrome.deb || apt-get install -yf \
    && rm chrome.deb \
    && rm -rf /var/lib/apt/lists/*

# Copy app code into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8000

# Start the app's uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
