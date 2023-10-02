# To-Do List API

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A feature-rich To-Do List API built with FastAPI and PostgreSQL, complete with authentication.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Authentication](#authentication)
  - [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication
- Create, read, update, and delete tasks
- Get a list of tasks for a user
- Task prioritization and due dates
- Secure and efficient storage with PostgreSQL

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.9 or higher installed
- PostgreSQL 13 or higher installed and running
- 

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/to-do-list-api.git
   ```

2. Navigate to the project directory:

  ```bash
  cd to-do-list-api
  ```

3. Install dependencies using pipenv:

```bash
pip install -r requirements.txt
```

4. Create a PostgreSQL database and configure the database connection in `config.py`

5. Run FastAPI Server
  ```bash
  uvicorn main:app --reload
  ```

# Usage
 
## Authentication
To use the API, you must first register and authenticate yourself.
- Register a new user: POST /user
- Authenticate: POST /login (Get a JWT token for authentication)
- Include the token in the Authorization header for protected endpoints.

## Endpoints
- Create a new task: POST /todos
- Get a Task by ID: GET /todos/{task_id}
- Get all tasks: GET /todos/
- Update Task: PUT /todos/{task_id}
- Delete Task: DELETE /todos/{task_id}
