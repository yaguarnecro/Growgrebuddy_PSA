# Development Tickets for GrowgrEbuddy_PSA MVP

## Core Features

### Ticket DEV-001: Set Up Development Environment
- **Description:** Set up the initial development environment for the project.
- **Who is in charge:** DevOps Engineer
- **Why:** This ticket is crucial for establishing a consistent development environment for all team members, ensuring that both frontend and backend can be developed and tested effectively.
- **Acceptance Criteria:**
  - Set up local development environments for frontend and backend
  - Configure Docker containers for consistent development across the team
  - Set up version control with Git and GitHub
  - Configure initial CI/CD pipeline using GitHub Actions
- **Complete**
  - [x] Marked as done
- **Results/Changes:**
  - Local development environments for frontend (Vue.js) and backend (Django) have been set up.
  - Docker containers have been configured and tested.
  - Version control has been established with Git and pushed to GitHub.
  - Initial CI/CD pipeline has been configured using GitHub Actions.

### Ticket DEV-002: Implement Frontend "Hello World"
- **Description:** Create a basic Vue.js application that displays "Hello World".
- **Who is in charge:** Frontend Developer
- **Why:** This ticket will help establish the frontend framework and ensure that the development environment is functioning correctly.
- **Acceptance Criteria:**
  - Set up a new Vue.js project
  - Create a component that renders "Hello World"
  - Ensure the application runs locally
- **Complete**
  - [x] 
- **Results/Changes:**
  - A new Vue.js component named `HelloWorld.vue` was created to display "Hello World".
  - The `HelloWorld` component was integrated into the main `App.vue` file.
  - The application was successfully run locally, displaying "Hello World" at `http://localhost:8080`.

### Ticket DEV-003: Implement Backend "Hello World"
- **Description:** Set up a Django server that responds with "Hello World".
- **Who is in charge:** Backend Developer
- **Why:** This ticket is essential for verifying that the backend environment is correctly configured and operational.
- **Acceptance Criteria:**
  - Create a new Django project
  - Set up a view that returns "Hello World"
  - Ensure the server runs locally and responds correctly
- **Complete**
  - [x] 
- **Results/Changes:**
  - A new view named `hello_world` was created in `views.py` that returns "Hello World".
  - The `urls.py` file was updated to include a new URL route (`/hello/`) that maps to the `hello_world` view.
  - The server was successfully run locally, and the endpoint returned "Hello World" when accessed at `http://127.0.0.1:8000/hello/`.

### Ticket DEV-004: Implement API "Hello World"
- **Description:** Create a RESTful API endpoint that returns "Hello World".
- **Who is in charge:** Full-stack Developer
- **Why:** This ticket will validate the API functionality and ensure that the frontend can communicate with the backend.
- **Acceptance Criteria:**
  - Create an API endpoint in Django that returns a JSON response with "Hello World"
  - Test the endpoint using Postman or similar tool
- **Complete**
  - [x] 
- **Results/Changes:**
  - A new API view named `hello_world_api` was created in `views.py` that returns a JSON response with "Hello World".
  - The `urls.py` file was updated to include a new URL route (`/api/hello/`) that maps to the `hello_world_api` view.
  - The server was successfully run locally, and the endpoint returned the expected JSON response when accessed at `http://127.0.0.1:8000/api/hello/`.

### Ticket DEV-005: Configure Docker for Frontend and Backend
- **Description**: Ensure that Docker is properly configured for both the Vue.js frontend and Django backend, including Dockerfiles and docker-compose setup.
- **Who is in charge**: DevOps Engineer
- **Why**: This ticket is essential for ensuring that the application can be run consistently across different environments using Docker.
- **Acceptance Criteria**:
  - Verify that the Dockerfile for the frontend is correctly set up.
  - Verify that the Dockerfile for the backend is correctly set up.
  - Ensure that the `docker-compose.yml` file can run both services together.
- **Complete**: [x] 
- **Results/Changes**:
  - The Dockerfile for the Vue.js frontend was verified and confirmed to be set up correctly.
  - The Dockerfile for the Django backend was created and confirmed to be set up correctly.
  - A `docker-compose.yml` file was created to manage both services, allowing them to run together.
  - The Docker setup was tested, and both services were successfully run locally.

### Ticket DEV-006: Update GitHub Actions CI/CD Pipeline
- **Description**: Update the GitHub Actions workflow to include steps for building and testing both the frontend and backend applications.
- **Who is in charge**: DevOps Engineer
- **Why**: This ticket is critical for automating the testing and deployment process, ensuring that the application is always in a deployable state.
- **Acceptance Criteria**:
  - Ensure that the CI workflow builds and tests the frontend application.
  - Ensure that the CI workflow builds and tests the backend application.
  - Add steps to build Docker images and push them to a container registry if applicable.
- **Complete**: [x] 
- **Results/Changes**:
  - The GitHub Actions workflow was updated to include steps for building and testing both the frontend and backend applications.
  - The workflow now installs dependencies and runs tests for both services.
  - The CI/CD pipeline was successfully tested and verified to run correctly.

## User Management

### Ticket DEV-005: User Authentication
- **Description:** Implement user registration and login functionality.
- **Who is in charge:** Backend Developer
- **Why:** This ticket is critical for user management and security within the application.
- **Acceptance Criteria:**
  - Develop user registration with email and password
  - Implement secure login system
  - Create password reset functionality
- **Complete**
  - [ ] 
- **Results/Changes:**
  - Document results after completion.

### Ticket DEV-006: User Profile Management
- **Description:** Create user profile functionality.
- **Who is in charge:** Full-stack Developer
- **Why:** This ticket will enhance user experience by allowing users to manage their profiles.
- **Acceptance Criteria:**
  - Develop user profile page
  - Allow users to update their information
  - Implement profile picture upload
- **Complete**
  - [ ] 
- **Results/Changes:**
  - Document results after completion.

## Game Features

### Ticket DEV-007: Implement Virtual Spaces
- **Description:** Develop "The Cave" and "Samsara" virtual spaces.
- **Who is in charge:** Frontend Developer
- **Why:** This ticket is important for creating engaging environments for users.
- **Acceptance Criteria:**
  - Create UI for both virtual spaces
  - Implement navigation between spaces
  - Develop basic interactions within each space
- **Complete**
  - [ ] 
- **Results/Changes:**
  - Document results after completion.

### Ticket DEV-008: Develop Mini-Games
- **Description:** Create "Memory Pairs" and "Simon Says Breath" mini-games.
- **Who is in charge:** Frontend Developer
- **Why:** This ticket will add interactive elements to the application, enhancing user engagement.
- **Acceptance Criteria:**
  - Implement game logic for both mini-games
  - Create engaging UI for the games
  - Integrate games with the point system
- **Complete**
  - [ ] 
- **Results/Changes:**
  - Document results after completion.

## Future Enhancement Tickets

### Ticket FUT-001: Implement Additional Virtual Spaces
- **Description:** Develop "The Reflections Biome" and "The Void" virtual spaces.
- **Priority:** Low (Future Enhancement)
- **Assignee:** TBD

### Ticket FUT-002: Expand Point System
- **Description:** Add Seeds and Droops to the existing point system.
- **Priority:** Low (Future Enhancement)
- **Assignee:** TBD

### Ticket FUT-003: Develop Additional Mini-Games
- **Description:** Create "Long List," "Infinite Bite Runner," and "Story Making" mini-games.
- **Priority:** Low (Future Enhancement)
- **Assignee:** TBD

## Ticket XX: Create Technical Diagrams [SDLC: Development]
- [ ] **Description:** Develop technical diagrams to support the development and implementation of GrowEbuddy PSA.
- **Priority:** High
- **Assignee:** John Smith (System Architect) and Development Team
- **Due Date:** TBD (To be scheduled during development phase)
- **Acceptance Criteria:**
  - Create Database Schema Diagram
  - Develop System Architecture Diagram
  - Design Sequence Diagrams for key processes
  - Create Class Diagrams (if using object-oriented programming)
  - Develop Deployment Diagram
- **Deliverables:**
  - Database Schema Diagram (PDF and editable format)
  - System Architecture Diagram (PDF and editable format)
  - Sequence Diagrams (PDF and editable format)
  - Class Diagrams (PDF and editable format)
  - Deployment Diagram (PDF and editable format)
- **Notes:**
  - Ensure all diagrams are consistent with the established system design and architecture
  - Update diagrams as needed throughout the development process
  - Consider creating additional diagrams as required by the development team
