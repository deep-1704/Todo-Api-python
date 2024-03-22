# Todo API

* This application features a todo API which makes it easy to create and manage daily tasks.

## Features

- Register/login
- Create, read, update, and delete tasks

## Authors

- [@deep-1704](https://github.com/deep-1704)

## Tech Stack

**Server:** Fast-Api

**Database:** MySql

**Authentication:** JWT

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DB_HOST` -- Database host (= localhost)

`DB_DATABASE` -- Name of the database

`DB_USERNAME` -- Username

`DB_PASSWORD` -- Password

`JWT_SECRET` -- Secret key for JWT algorithm (You can add any random string)

## Run Locally

#### Before you start:

- Make sure to have Python and MySql-DB preinstalled in your system.

#### Steps:

Clone the project

```bash
  git clone https://github.com/deep-1704/Todo-Api-python.git
```

Go to the project directory

```bash
  cd Todo-Api-python
```

Install dependencies

```bash
  pip install -r requirements.txt
```

- Please ensure the `.env` file in root folder

Database setup:

- In order to setup database tables, execute `script.sql` file present in `/SQL` directory.
- (Optional) Execute `sample_data.sql` file to populate sample data.

Run app

```bash
  uvicorn main:app --reload
```

API is now up and running on port 8000.

## API Reference

#### 1. Register new user

```http
  POST /api/auth/register
```

**Request:**

Body: {username, password}

**Response:**

If user already exists -- `400_BAD_REQUEST` {"message": "User already exists"}

For new user -- `201_CREATED`{"token": JWT-token}

#### 2. User login

```http
  POST /api/auth/login
```

**Request:**

Body: {username, password}

**Response:**

If user not found -- `404_NOT_FOUND` {"message": "User not found"}

If incorrect password -- `401_UNAUTHORIZED`{"message": "Invalid password"}

Successful login -- `201_CREATED`{"token": JWT-token}

#### 3. Get all tasks

```http
  GET /api/task
```

**Request:**

Header: {Authorization: "Bearer [JWT-token]"}

**Response:**

`200_OK` [array of tasks]

#### 4. Get task by id

```http
  GET /api/task/{task_id}
```

**Request:**

Header: {Authorization: "Bearer [JWT-token]"}

**Response:**

`200_OK` {id, username, description, status}

#### 5. Create new task

```http
  POST /api/task
```

**Request:**

Header: {Authorization: "Bearer [JWT-token]"}

Body: {id: null, username, description, status}

**Response:**

`201_CREATED` {"message": "Task created"}

#### 6. Update task description

```http
  PUT /api/task/update_description/{task_id}
```

**Request:**

Header: {Authorization: "Bearer [JWT-token]"}

Body: {id, username, description, status}

**Response:**

`200_OK` {"message": "Task description updated"}

#### 7. Update task status

```http
  PUT /api/task/update_status/{task_id}
```

**Request:**

Header: {Authorization: "Bearer [JWT-token]"}

Body: {id, username, description, status}

**Response:**

`200_OK` {"message": "Task status updated"}

#### 8. Delete task

```http
  DELETE /api/task/{task_id}
```

**Request:**

Header: {Authorization: "Bearer [JWT-token]"}

**Response:**

`200_OK` {"message": "Task deleted"}
