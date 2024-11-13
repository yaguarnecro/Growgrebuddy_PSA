# Dockerfile for Vue.js Frontend
# This Dockerfile sets up the environment for the Vue.js application.

FROM node:14  # Use the official Node.js 14 image as the base image
WORKDIR /app  # Set the working directory inside the container

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install the dependencies defined in package.json
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Command to run the application
CMD ["npm", "run", "serve"]  # Start the Vue.js development server

    