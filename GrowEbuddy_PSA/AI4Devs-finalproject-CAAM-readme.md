# GrowgrEbuddy_PSA Project Documentation

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Product Description](#2-product-description)
3. [System Architecture](#3-system-architecture)
4. [Data Model](#4-data-model)
5. [API Specification](#5-api-specification)
6. [User Stories](#6-user-stories)
7. [Work Tickets](#7-work-tickets)
8. [Pull Requests](#8-pull-requests)

## 1. Project Overview

### 1.1 Your Full Name
Carlos Arturo Araque Montoya

### 1.2 Project Name
GrowgrEbuddy_PSA

### 1.3 Brief Project Description
GrowgrEbuddy_PSA is a gamified personal development application that combines elements of virtual pet care, habit tracking, and mental wellness to help users improve their overall well-being.

### 1.3.1 Project Scope
The current project scope focuses on implementing the following key features:

- **Virtual Mascot**: A dynamic mascot that evolves based on user progress and interactions.
- **Virtual Spaces**: Interactive environments like "The Cave" for introspection and "Samsara" for life challenges.
- **User Progression**: A system that rewards users with daily login bonuses, streaks, and achievements.

### 1.4 Project URL
www.growgrebuddy.com?

### 1.5 Repository URL or Compressed File
[GrowgrEbuddy Play Systeme App](https://github.com/yaguarnecro/Growgrebuddy_PSA)

## 2. Product Description

### 2.1 Objective
The primary objectives of GrowgrEbuddy_PSA are:
1. To encourage users to engage in daily personal development activities.
2. To promote mental wellness through guided exercises and reflection.
3. To foster habit formation through gamification and rewards.
4. To provide a sense of progress and achievement in personal growth.

### 2.2 Main Features and Functionalities

#### MVP Features
1. **Virtual Mascot**: Evolves based on user progress and interactions.
2. **Virtual Spaces**: "The Cave" for introspection and "Samsara" for life challenges.
3. **User Progression System**: Levels, achievements, and customization options.
4. **Point System**: EXP for progress and Coins for in-app purchases.
5. **Daily Challenges and Habit Tracking**: Encourages consistent personal development activities.

#### Future Enhancements
1. **Mini-Games**: Memory Pairs and Simon Says Breath.
2. **Mood Tracking and Guided Meditations**: Supports mental wellness through reflection and mindfulness exercises.

### 2.3 Design and User Experience
The design of GrowgrEbuddy_PSA focuses on creating an engaging and intuitive user experience. Key design principles include:

- **Simplicity**: A clean and minimalist interface that is easy to navigate.
- **Consistency**: Uniform design patterns and elements across the application, utilizing Vuetify components.
- **Feedback**: Immediate and clear feedback for user actions to enhance interactivity.
- **Accessibility**: Ensuring the app is usable by people with diverse abilities.
- **Visual Style Guide**: Consistent use of color palette and typography to maintain a cohesive look.
- **Responsive Design**: Mobile-first approach with a responsive grid system for various devices.

[Insert screenshots, wireframes, or links to video tutorials showcasing the user experience]

### 2.4 Installation Instructions

To set up the GrowgrEbuddy_PSA project locally, follow these steps:

#### Prerequisites
- Ensure you have the following installed on your machine:
  - **Node.js** (version X.X.X or higher)
  - **Python** (version X.X or higher)
  - **PostgreSQL** (version X.X or higher)
  - **Docker** (optional, for containerization)

#### Step 1: Clone the Repository
Open your terminal and run the following command to clone the repository:

```bash
git clone https://github.com/yaguarnecro/Growgrebuddy_PSA
```

## 3. System Architecture

### 3.1 Architecture Diagram
The architecture of GrowgrEbuddy_PSA consists of the following components:

- **Frontend**: Built with Vue.js and Vuetify, providing a responsive user interface.
- **Backend**: Developed using Django, serving RESTful APIs to handle requests from the frontend.
- **Database**: PostgreSQL is used for data storage, ensuring data integrity and reliability.
- **Deployment**: The application is hosted on Heroku, allowing for easy scaling and management.
- **Containerization**: Docker is utilized to ensure consistent environments across development, testing, and production.

![Architecture Diagram](path/to/your/architecture_diagram.png)  <!-- Replace with the actual path to your diagram -->

+-------------------+          +-------------------+
|                   |          |                   |
|   Frontend        | <------> |   Backend         |
|   (Vue.js)        |          |   (Django)       |
|                   |          |                   |
+-------------------+          +-------------------+
          |                             |
          |                             |
          |                             |
          v                             v
+-------------------+          +-------------------+
|                   |          |                   |
|   User Interface   |          |   REST API        |
|   (Vuetify)       |          |                   |
|                   |          |                   |
+-------------------+          +-------------------+
          |                             |
          |                             |
          v                             v
+-------------------+          +-------------------+
|                   |          |                   |
|   PostgreSQL      | <------> |   Docker          |
|   (Database)      |          |   (Containerization)|
|                   |          |                   |
+-------------------+          +-------------------+

### 3.2 Main Components Description
- **Frontend**: 
  - **Vue.js with JavaScript**: A progressive JavaScript framework for building user interfaces, allowing for a reactive and dynamic user experience.
  - **Vuetify**: A Material Design component framework for Vue.js, providing pre-built accessible components that speed up development.

- **Backend**: 
  - **Python**: A versatile programming language that is easy to learn and use.
  - **Django**: A high-level Python web framework that provides a robust foundation for building web applications, ensuring rapid development and clean design.
  - **Django REST Framework**: A powerful toolkit for building Web APIs, enabling seamless communication between the frontend and backend.

- **Database**: 
  - **PostgreSQL**: A powerful, open-source relational database management system that ensures data integrity and supports complex queries.

- **Deployment**: 
  - **Heroku**: A cloud platform as a service (PaaS) that simplifies the deployment, management, and scaling of web applications.

- **Containerization**: 
  - **Docker**: A tool designed to make it easier to create, deploy, and run applications by using containers, ensuring consistent environments across development, testing, and production.



### 3.3 High-Level Project Description and File Structure

The GrowgrEbuddy_PSA project is organized into several key directories, each serving a specific purpose. Below is an overview of the project's file structure:

```
GrowEbuddy_PSA/
├── frontend/                  # Contains the frontend application built with Vue.js
│   ├── src/                  # Source files for the Vue.js application
│   ├── public/               # Public assets and index.html
│   ├── package.json           # Frontend dependencies and scripts
│   └── ...
├── backend/                   # Contains the backend application built with Django
│   ├── api/                  # API endpoints and views
│   ├── models/               # Database models
│   ├── migrations/           # Database migrations
│   ├── settings.py           # Django settings configuration
│   └── ...
├── docs/                      # Documentation files
│   ├── api/                  # API documentation
│   ├── development/          # Development-related documents
│   └── ...
├── tests/                     # Test cases for both frontend and backend
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── ...
├── scripts/                   # Utility scripts for development and deployment
├── .gitignore                 # Git ignore file
├── README.md                  # Project overview and instructions
└── docker-compose.yml         # Docker configuration for the application
```

#### Directory Descriptions:
- **frontend/**: Contains the source code for the Vue.js application, including components, views, and assets.
- **backend/**: Contains the Django application, including models, views, and API endpoints.
- **docs/**: Holds all documentation related to the project, including API documentation and development guides.
- **tests/**: Contains test cases for both the frontend and backend, organized into unit and integration tests.
- **scripts/**: Utility scripts that assist with development tasks, such as database seeding or deployment scripts.
- **.gitignore**: Specifies files and directories that should be ignored by Git.
- **README.md**: Provides an overview of the project, installation instructions, and other relevant information.
- **docker-compose.yml**: Configuration file for Docker, defining services, networks, and volumes for the application.

This structure ensures that the project is organized and maintainable, making it easier for developers to navigate and contribute to the codebase.

### 3.4 Infrastructure and Deployment
The GrowgrEbuddy_PSA application is deployed on Heroku, utilizing Docker containers to ensure consistent environments across development, testing, and production. The deployment process includes:

- **Docker Compose**: Used to define and run multi-container Docker applications, simplifying the setup of the development environment.
- **Heroku**: The application is hosted on Heroku, which provides a cloud platform as a service (PaaS) for easy scaling and management.
- **Continuous Integration/Continuous Deployment (CI/CD)**: GitHub Actions are configured to automate testing and deployment processes, ensuring that code changes are automatically tested and deployed to Heroku.

### 3.5 Security
The application implements several security measures to protect user data and ensure safe interactions:

- **Data Encryption**: User data is encrypted both at rest and in transit to prevent unauthorized access.
- **Authentication**: A secure authentication system is implemented using OAuth 2.0, allowing users to log in safely.
- **Privacy Settings**: Users have control over their shared information, with options to manage privacy settings.
- **Data Management**: Users can export or delete their data upon request, ensuring compliance with data protection regulations.

### 3.6 Tests
The testing strategy for GrowgrEbuddy_PSA includes various testing methodologies to ensure the application is robust and reliable:

- **Unit Testing**: 
  - **Frontend**: Jest is used for unit testing Vue.js components, ensuring that each component functions as expected.
  - **Backend**: Pytest is utilized for unit testing Django models and views, verifying the correctness of backend logic.

- **Integration Testing**: 
  - **Frontend**: Cypress is employed for integration testing of user interactions within the Vue.js application.
  - **Backend**: Pytest is also used for integration tests to ensure that API endpoints work correctly with the database.

- **System Testing**: Selenium WebDriver is used for end-to-end testing, simulating user interactions with the application to validate the overall functionality.

- **User Acceptance Testing**: Beta testers provide feedback through in-app feedback forms, allowing for real-world testing and validation of user stories.

## 4. Data Model

### 4.1 Data Model Diagram
The data model for GrowgrEbuddy_PSA is designed to support the application's core features, including the virtual mascot, user progression, and habit tracking. Below is the Entity-Relationship Diagram (ERD) representing the main entities and their relationships.

![Data Model Diagram](path/to/your/data_model_diagram.png)  <!-- Replace with the actual path to your ERD -->

### 4.2 Main Entities Description
The following are the main entities in the data model:

1. **User**
   - **Attributes**:
     - `user_id`: Unique identifier for the user (Primary Key)
     - `username`: The user's chosen name
     - `email`: The user's email address
     - `password_hash`: Hashed password for authentication
     - `created_at`: Timestamp of account creation
   - **Relationships**:
     - One-to-Many with **Mascot** (a user can have one mascot)

2. **Mascot**
   - **Attributes**:
     - `mascot_id`: Unique identifier for the mascot (Primary Key)
     - `user_id`: Foreign key referencing the User entity
     - `level`: Current level of the mascot
     - `experience_points`: Points accumulated by the mascot
     - `mood`: Current mood state of the mascot
   - **Relationships**:
     - Many-to-One with **User**

3. **Habit**
   - **Attributes**:
     - `habit_id`: Unique identifier for the habit (Primary Key)
     - `user_id`: Foreign key referencing the User entity
     - `name`: Name of the habit
     - `frequency`: How often the habit should be performed (e.g., daily, weekly)
     - `streak`: Current streak of habit completion
   - **Relationships**:
     - Many-to-One with **User**

4. **Challenge**
   - **Attributes**:
     - `challenge_id`: Unique identifier for the challenge (Primary Key)
     - `user_id`: Foreign key referencing the User entity
     - `description`: Description of the challenge
     - `points_reward`: Points awarded upon completion
     - `is_completed`: Boolean indicating if the challenge has been completed
   - **Relationships**:
     - Many-to-One with **User**

This data model supports the core functionalities of the GrowgrEbuddy_PSA application, allowing for user management, mascot evolution, habit tracking, and challenge completion.

## 5. API Specification

The GrowgrEbuddy_PSA application exposes several RESTful API endpoints to facilitate communication between the frontend and backend. Below are the specifications for the main API endpoints. Note that user authentication endpoints are currently mocked and not implemented.

### 1. User Authentication (Mocked)

- **Endpoint**: `/api/auth/register`
  - **Method**: POST
  - **Request Body**:
    ```json
    {
      "username": "string",
      "email": "string",
      "password": "string"
    }
    ```
  - **Response**:
    - **200 OK**: User registration is mocked.
      ```json
      {
        "message": "User registration is currently mocked."
      }
      ```

- **Endpoint**: `/api/auth/login`
  - **Method**: POST
  - **Request Body**:
    ```json
    {
      "email": "string",
      "password": "string"
    }
    ```
  - **Response**:
    - **200 OK**: User login is mocked.
      ```json
      {
        "message": "User login is currently mocked."
      }
      ```

### 2. Mascot Management

- **Endpoint**: `/api/mascot`
  - **Method**: GET
  - **Headers**: 
    - `Authorization: Bearer <token>`
  - **Response**:
    - **200 OK**: Returns the user's mascot details.
      ```json
      {
        "mascot_id": "string",
        "level": "number",
        "experience_points": "number",
        "mood": "string"
      }
      ```

### 3. Habit Tracking

- **Endpoint**: `/api/habits`
  - **Method**: POST
  - **Headers**: 
    - `Authorization: Bearer <token>`
  - **Request Body**:
    ```json
    {
      "name": "string",
      "frequency": "string"
    }
    ```
  - **Response**:
    - **201 Created**: Habit successfully created.
      ```json
      {
        "habit_id": "string",
        "message": "Habit created successfully."
      }
      ```
    - **400 Bad Request**: Validation errors.
      ```json
      {
        "error": "Validation error message."
      }
      ```

This API specification provides a clear overview of the key endpoints that will be used in the GrowgrEbuddy_PSA application, facilitating communication between the frontend and backend components.

## 6. User Stories

### User Story 1
As a user, I want to interact with a virtual mascot that evolves based on my progress, so that I can feel a sense of connection and achievement in my personal development journey.

### User Story 2
As a user, I want to access different virtual spaces, such as "The Cave" for introspection and "Samsara" for life challenges, so that I can engage in activities that promote my mental wellness and personal growth.

### User Story 3
As a user, I want to track my daily habits and receive rewards for completing them, so that I can stay motivated and build positive routines.

### User Story 4
As a user, I want to set daily challenges for myself, so that I can push my boundaries and achieve personal growth goals.

### User Story 5
As a user, I want to monitor my mascot's mood and progress, so that I can understand how my actions impact my personal development journey.

## 7. Work Tickets

### Ticket 1 (Backend)
**Ticket DEV-004: User Authentication**
- **Description:** Implement user registration and login functionality.
- **Priority:** High
- **Assignee:** Backend Developer
- **Acceptance Criteria:**
  - Develop user registration with email and password
  - Implement secure login system
  - Create password reset functionality

### Ticket 2 (Frontend)
**Ticket DEV-002: Implement Virtual Mascot**
- **Description:** Develop the core virtual mascot feature.
- **Priority:** High
- **Assignee:** Frontend Developer
- **Acceptance Criteria:**
  - Create basic mascot design with emoticon-based expressions
  - Implement mascot evolution based on user progress
  - Develop mascot interaction animations and sounds

### Ticket 3 (Database)
**Ticket DEV-003: Develop Point System**
- **Description:** Implement the EXP and Coins system.
- **Priority:** High
- **Assignee:** Full-stack Developer
- **Acceptance Criteria:**
  - Create backend logic for earning and spending points
  - Develop frontend UI for displaying user points
  - Implement point transactions for completing activities and purchasing items

## 8. Pull Requests

### Pull Request 1
[Insert pull request details]

### Pull Request 2
[Insert pull request details]

### Pull Request 3
[Insert pull request details]
