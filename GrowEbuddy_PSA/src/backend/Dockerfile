# Dockerfile for Django Backend
# This Dockerfile sets up the environment for the Django application.

FROM python:3.9  # Use the official Python 3.9 image as the base image
WORKDIR /app  # Set the working directory inside the container

# Copy requirements.txt to the working directory
COPY requirements.txt ./

# Install the dependencies defined in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]  # Start the Django development server