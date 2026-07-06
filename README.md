# El-Task-04

# Task 4: REST API with Flask

## Objective

Create a REST API to manage user data using Python and Flask.

## Tools Used

* Python
* Flask
* Postman / Curl (for testing)

## Description

This project implements a simple REST API that performs CRUD operations (Create, Read, Update, Delete) on user data. The user information is stored in an in-memory dictionary.

## API Endpoints

| Method | Endpoint    | Description         |
| ------ | ----------- | ------------------- |
| GET    | /           | Check API status    |
| GET    | /users      | Get all users       |
| GET    | /users/<id> | Get a specific user |
| POST   | /users      | Add a new user      |
| PUT    | /users/<id> | Update user         |
| DELETE | /users/<id> | Delete user         |

## How to Run

1. Install Flask:

   ```
   pip install flask
   ```
2. Run the application:

   ```
   python app.py
   ```
3. Open browser:

   ```
   http://127.0.0.1:5000/
   ```

## Outcome

* Learned REST API development fundamentals
* Understood HTTP methods (GET, POST, PUT, DELETE)
* Gained experience with Flask routing and JSON responses
