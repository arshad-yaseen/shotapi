# Use an official Python runtime as a base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Chromium for Puppeteer
RUN pyppeteer-install

# Make port 80 available to the world outside this container
EXPOSE 80

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
