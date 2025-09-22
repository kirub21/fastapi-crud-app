# FastAPI CRUD Application

## Overview

A simple FastAPI application to perform CRUD operations on Students and Courses.

## Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/kirub21/fastapi-crud-app.git
   cd fastapi-crud-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

For full interactive API documentation, visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Students

- `POST /students/` - Create a new student  
  Request Body:  
  ```json
  {
    "name": "Jane Doe",
    "email": "jane@example.com"
  }
  ```

- `GET /students/` - List all students

- `GET /students/{student_id}` - Get a student by ID

- `DELETE /students/{student_id}` - Delete a student

### Courses

- `POST /courses/` - Create a new course  
  Request Body:  
  ```json
  {
    "title": "Math 101",
    "student_id": 1
  }
  ```

- `GET /courses/` - List all courses

- `GET /courses/{course_id}` - Get a course by ID

- `DELETE /courses/{course_id}` - Delete a course

## Database

- Uses SQLite for demonstration (`test.db` will be created in the project root).  
- You can switch to PostgreSQL or MySQL by changing the `DATABASE_URL` in `app/database.py`.
