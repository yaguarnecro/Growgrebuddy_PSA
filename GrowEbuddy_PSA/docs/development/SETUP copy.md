# Project Setup and Running Instructions

To successfully run your application, you need to ensure that several components are up and running. Here’s an overview of what needs to be running, why each component is necessary, and how to set them up in your project on Windows OS.

## Overview of Components to Run

### 1. Docker:
- **Why:** Docker is used to containerize your application, including the PostgreSQL database. This ensures that your application runs in a consistent environment across different machines.
- **How:** You will run Docker to start the PostgreSQL container defined in your `docker-compose.yml` file.

### 2. PostgreSQL Database Server:
- **Why:** This is the database that your application will use to store and retrieve data. It needs to be running for your backend to connect and perform operations.
- **How:** If you are using Docker, the PostgreSQL server will run inside a Docker container. If not using Docker, ensure that the PostgreSQL service is running on your machine.

### 3. Backend Server (Django):
- **Why:** The backend server handles API requests from the frontend and interacts with the database. It needs to be running to serve the API endpoints.
- **How:** You will run the Django development server using the command `python manage.py runserver`. **This command must be run in the terminal where your virtual environment is activated.**

### 4. Frontend Application:
- **Why:** The frontend application (built with Vue.js or another framework) interacts with the backend API to provide a user interface. It needs to be running to allow users to interact with your application.
- **How:** You will run the frontend server using the appropriate command (e.g., `npm run serve`).

### 5. Prisma Client:
- **Why:** The Prisma client is used to interact with the database from your backend code. It needs to be generated and available for your backend to function correctly.
- **How:** You will generate the Prisma client using the command `npx prisma generate` after running migrations. **This command should also be run in the terminal where your virtual environment is activated.**

### 6. Virtual Environment:
- **Why:** The virtual environment isolates your Python dependencies, ensuring that your project uses the correct versions of libraries without conflicts.
- **How:** You will activate the virtual environment before running your Django server or any other Python-related commands.

## Step-by-Step Instructions to Set Up Your Project

### Step 1: Start Docker
- **Open Docker Desktop:** Ensure Docker Desktop is running on your machine. You should see the Docker icon in your system tray.
- **Run Docker Compose:** Open a terminal (this can be any terminal) and navigate to your project directory:
  - Run the following command to start all services, including the PostgreSQL container:
  ```bash
  docker-compose up -d
  ```

### Step 1.1: Start PostgreSQL Service
- Ensure the PostgreSQL service is defined in your `docker-compose.yml`.
- The PostgreSQL service will automatically start with the `docker-compose up -d` command.

### Step 2: Activate the Virtual Environment
- Open a new terminal (or use the same one if you prefer) and navigate to the backend directory or the directory that contains the `venv` file (folder src/):
- Activate your virtual environment:
```bash
cd C:\Users\yagua\AI4Devs\Growgrebuddy_PSA\GrowEbuddy_PSA\src\
.\venv\Scripts\Activate.ps1
```

### Step 3: Run Prisma Migrations
- **Important**: This command should be run in the terminal where your virtual environment is activated.
- Run the Prisma migration command to ensure your database schema is up to date:
```bash
cd C:\Users\yagua\AI4Devs\Growgrebuddy_PSA\GrowEbuddy_PSA\src\backend\prisma
npx prisma migrate dev --name init
npx prisma generate
```

### Step 4: Start the Django Backend Server
- **Important**: This command should also be run in the terminal where your virtual environment is activated.
- **Run the Django development server from the `src/backend` directory: where the manage.py file is located**
```bash
cd C:\Users\yagua\AI4Devs\Growgrebuddy_PSA\GrowEbuddy_PSA\src\
python manage.py runserver
```

### Step 5: Start the Frontend Application
- Open another terminal (this can be any terminal) and navigate to your frontend directory (if applicable):
```bash
cd C:\Users\yagua\AI4Devs\Growgrebuddy_PSA\GrowEbuddy_PSA\src\frontend
npm run serve
```

## Summary of Commands

Here’s a summary of the commands you will run in your terminal:

1. **Start Docker:**
   ```bash
   cd C:\Users\yagua\AI4Devs\Growgrebuddy_PSA\GrowEbuddy_PSA
   docker-compose up -d
   ```
2. **Activate Virtual Environment:**
   ```bash
   cd C:\Users\yagua\AI4Devs\Growgrebuddy_PSA\GrowEbuddy_PSA\src\
   .\venv\Scripts\Activate.ps1
   ```
   2.1. **Run Prisma Migrations:**  <!-- This command should be run in the terminal where your virtual environment is activated -->
   ```bash
   cd C:\Users\yagua\AI4Devs\Growgrebuddy_PSA\GrowEbuddy_PSA\src\backend\prisma
   npx prisma migrate dev --name init
   npx prisma generate
   ```
   2.2. **Run Django Server:**  <!-- This command should also be run in the terminal where your virtual environment is activated -->
   ```bash
   cd C:\Users\yagua\AI4Devs\Growgrebuddy_PSA\GrowEbuddy_PSA\src\
   python manage.py runserver
   ```
3. **Run Frontend Server:**
   ```bash
   cd C:\Users\yagua\AI4Devs\Growgrebuddy_PSA\GrowEbuddy_PSA\src\frontend
   npm run serve
   ```

## Turning Off the Setup

To properly shut down your application and its components, follow these steps:

1. **Stop Frontend Server:**
   - In the terminal where the frontend server is running, press `Ctrl + C` to stop it.

2. **Stop Django Server:**
   - In the terminal where the Django server is running, press `Ctrl + C` to stop it.

3. **Deactivate Virtual Environment:**
   - Simply type `deactivate` in the terminal to exit the virtual environment.

4. **Stop Docker Containers:**
   - Run the following command to stop and remove the Docker containers:
   ```bash
   docker-compose down
   ```

Following these steps will ensure that all components of your application are properly shut down. 