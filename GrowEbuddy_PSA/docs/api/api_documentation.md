# API Documentation for GrowEbuddy P.S.A.

## Overview
This document provides detailed information about the APIs used or provided by the GrowEbuddy P.S.A. system.

## API Endpoints

### Endpoint 1: Get User Profile
- **URL**: `/api/v1/user/profile`
- **Method**: GET
- **Description**: Retrieves the profile information of the authenticated user.
- **Request Headers**:
  - `Authorization`: Bearer token
- **Response**:  ```json
  {
    "id": "user123",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "avatar": "url_to_avatar"
  }  ```

### Endpoint 2: Update User Profile
- **URL**: `/api/v1/user/profile`
- **Method**: PUT
- **Description**: Updates the profile information of the authenticated user.
- **Request Headers**:
  - `Authorization`: Bearer token
- **Request Body**:  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "avatar": "url_to_avatar"
  }  ```
- **Response**:  ```json
  {
    "message": "Profile updated successfully"
  }  ```

### Endpoint 3: List User Activities
- **URL**: `/api/v1/user/activities`
- **Method**: GET
- **Description**: Retrieves a list of activities for the authenticated user.
- **Request Headers**:
  - `Authorization`: Bearer token
- **Response**:  ```json
  [
    {
      "activityId": "activity123",
      "type": "exercise",
      "duration": 30,
      "date": "2024-10-15"
    },
    ...
  ]  ```

## Review and Approval
- **Reviewed by**: [Development Team Member Names]
- **Approval Date**: [Date] 