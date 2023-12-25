FROM python:3.12

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Use pyppeteer-install to install Chromium
RUN pyppeteer-install

# Copy the rest of your application's code
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define the command to run your application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
