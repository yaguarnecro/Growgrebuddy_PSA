# SETUPv2.md

## Overview
This document serves as a comprehensive guide to set up the GrowEbuddy_PSA project both locally and using Docker. It outlines the steps for configuring your environment, running the application, and managing different environments effectively.

---

## Local Setup

### Prerequisites
- **Python** (version 3.8 or higher)
- **PostgreSQL** (version 12 or higher)
- **Node.js** (for frontend development)
- **pip** (Python package installer)

### Steps to Set Up Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yaguarnecro/Growgrebuddy_PSA
   cd Growgrebuddy_PSA
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   cd src
   python -m venv venv
   .\venv\Scripts\activate  # For Windows
   ```

3. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL**:
   - **Create a New PostgreSQL Database**:
     ```sql
     CREATE DATABASE GrowEbuddy_PSA_DB;
     ```
   - **Create a New User and Grant Privileges**:
     ```sql
     CREATE USER your_user WITH PASSWORD 'your_password';
     GRANT ALL PRIVILEGES ON DATABASE GrowEbuddy_PSA_DB TO your_user;
     ```

5. **Configure Environment Variables**:
   - Update the `.env` file in `src/backend/prisma/`:
     ```plaintext
     DATABASE_URL=postgres://your_user:your_password@localhost:5432/GrowEbuddy_PSA_DB
     SECRET_KEY=your-secret-key
     DEBUG=True
     ```

6. **Run Prisma Migrations**:
   ```bash
   cd backend/prisma
   npx prisma migrate dev --name init
   npx prisma generate
   ```

7. **Run the Django Development Server**:
   ```bash
   cd ../..
   python manage.py runserver
   ```

---

## Docker Setup

### Steps to Set Up with Docker

1. **Ensure Docker is Installed**:
   - Make sure Docker Desktop is running on your machine.

2. **Configure Docker Compose**:
   - Update the `docker-compose.yml` file to include the PostgreSQL service:
   ```yaml
   version: '3.8'

   services:
     postgres:
       image: postgres:latest
       environment:
         POSTGRES_USER: your_user
         POSTGRES_PASSWORD: your_password
         POSTGRES_DB: GrowEbuddy_PSA_DB
       ports:
         - "5433:5432"  # Map the container's port 5432 to your host's port 5433

     backend:
       build:
         context: ./src/backend
       environment:
         DATABASE_URL: postgres://your_user:your_password@postgres:5432/GrowEbuddy_PSA_DB
       ports:
         - "8000:8000"

     frontend:
       build:
         context: ./src/frontend
       ports:
         - "8080:8080"
   ```

3. **Start Docker Containers**:
   ```bash
   docker-compose up -d
   ```

4. **Run Prisma Migrations in Docker**:
   - Execute the following command to run migrations inside the backend container:
   ```bash
   docker-compose exec backend npx prisma migrate dev --name init
   ```

5. **Run the Django Server in Docker**:
   ```bash
   docker-compose exec backend python manage.py runserver 0.0.0.0:8000
   ```

---

## Managing Different Environments in Docker

### Development Workflow

1. **Develop Locally**:
   - Make changes to your code in the local environment.
   - Test your changes by running the Django development server locally.

2. **Deploy to Docker**:
   - Once you are satisfied with your changes, commit them to your version control system.
   - Build and start your Docker containers:
   ```bash
   docker-compose up --build -d
   ```

3. **Run Migrations in Docker**:
   - After deploying, ensure that your database schema is up to date by running migrations in the Docker environment:
   ```bash
   docker-compose exec backend npx prisma migrate dev --name init
   ```

4. **Manage Different Environments**:
   - Use different `.env` files for different environments (development, testing, production) and update your `docker-compose.yml` to load the appropriate environment variables.

---

## Turning Off Docker Services

To stop and remove all running containers, use the following command:
```bash
docker-compose down
```
This command will stop all services defined in your `docker-compose.yml` file and remove the containers.

---

## Conclusion

This guide provides a comprehensive overview of setting up the GrowEbuddy_PSA project both locally and using Docker. By following these steps, you can efficiently develop, test, and deploy your application while managing different environments effectively.