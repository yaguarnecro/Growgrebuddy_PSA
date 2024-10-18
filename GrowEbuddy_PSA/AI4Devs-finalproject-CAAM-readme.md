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

### 1.4 Project URL
[Insert project URL here]

### 1.5 Repository URL or Compressed File
[Insert repository URL or instructions for accessing the repository]

## 2. Product Description

### 2.1 Objective
The primary objectives of GrowgrEbuddy_PSA are:
1. To encourage users to engage in daily personal development activities.
2. To promote mental wellness through guided exercises and reflection.
3. To foster habit formation through gamification and rewards.
4. To provide a sense of progress and achievement in personal growth.
5. To create a supportive community of users working towards self-improvement.

### 2.2 Main Features and Functionalities
1. Virtual Mascot: Evolves based on user progress and interactions
2. Virtual Spaces: "The Cave" for introspection and "Samsara" for life challenges
3. Point System: EXP for progress and Coins for in-app purchases
4. Mini-Games: Memory Pairs and Simon Says Breath
5. User Progression System: Levels, achievements, and customization options
6. Daily Challenges and Habit Tracking
7. Mood Tracking and Guided Meditations
8. Basic Social Features: Friends list, activity feed, and challenges

### 2.3 Design and User Experience
[Insert screenshots, wireframes, or links to video tutorials showcasing the user experience]

### 2.4 Installation Instructions
[Provide step-by-step instructions for setting up the project locally]

## 3. System Architecture

### 3.1 Architecture Diagram
[Insert architecture diagram here]

### 3.2 Main Components Description
- Frontend: Vue.js with JavaScript, Vuetify component library
- Backend: Python with Django and Django REST Framework
- Database: PostgreSQL
- Deployment: Heroku
- Containerization: Docker

### 3.3 High-Level Project Description and File Structure
[Provide an overview of the project's file structure and explain the purpose of main directories]

### 3.4 Infrastructure and Deployment
The application is deployed on Heroku, with Docker containers ensuring consistent environments across development, testing, and production.

### 3.5 Security
- User data encryption at rest and in transit
- Secure authentication system
- Privacy settings for user control over shared information
- Option for users to export or delete their data

### 3.6 Tests
- Unit Testing: Jest for frontend, pytest for backend
- Integration Testing: Cypress for frontend, pytest for backend
- System Testing: Selenium WebDriver
- User Acceptance Testing: Beta testers with in-app feedback forms

## 4. Data Model

### 4.1 Data Model Diagram
[Insert ERD here, preferably using Mermaid syntax]

### 4.2 Main Entities Description
[Describe main entities, their attributes, relationships, and constraints]

## 5. API Specification

[Describe up to 3 main API endpoints using OpenAPI format]

## 6. User Stories

### User Story 1
As a busy young professional, I want to easily track my daily habits and mood, so that I can see my progress over time and stay motivated.

### User Story 2
As a meditation beginner, I want guided mindfulness exercises, so that I can learn to manage stress and improve my focus.

### User Story 3
As a user interested in self-reflection, I want prompts and exercises that encourage introspection, so that I can gain deeper insights into myself.

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
