# Employee Management API

A Django REST Framework (DRF) based Employee Management System that provides authentication, role management, employee management, and but not now permission-based access control.

## Features

* User Authentication
* Role Management
* Employee Management
* Validation Layer
* Transaction Management
* PostgreSQL database
* RESTful API

---

## Technology Stack

* Python 3.x
* Django
* Django REST Framework
* PostgreSQL

---

## Installation

### Clone Repository

```bash
git git remote add origin https://github.com/bhimpdrajbanshi/HR-management-system-API-DRF-.git
cd HR-management-system-API-DRF
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment:

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create `.env`

```env
DEBUG=True

SECRET_KEY=your-secret-key

DB_NAME=employee_db
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```

### Run Migration

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Start Server

```bash
python manage.py runserver
```

---

## Authentication

Session Authentication

Login Endpoint:

```http
POST /api/login/
```

Request

```json
{
    "email": "admin@example.com",
    "password": "password"
}
```

Response

```json
{
    "success": true,
    "message": "Login successful"
}
```

---

## Role API

### Get Roles

```http
GET /api/roles/
```

Response

```json
{
    "success": true,
    "message": "Role list fetched successfully",
    "data": [
        {
            "id": 1,
            "role_name": "Admin",
            "status": "active"
        }
    ]
}
```

### Create Role

```http
POST /api/roles/create/
```

Request

```json
{
    "role_name": "Manager"
}
```

Response

```json
{
    "success": true,
    "message": "Role created successfully",
    "data": {
        "id": 2,
        "role_name": "Manager",
        "status": "active"
    }
}
```

---

## Employee API

### Create Employee

```http
POST /api/employees/create/
```

Request

```json
{
    "email": "employee@example.com",
    "username": "employee01",
    "role_id": 1,
    "first_name": "John",
    "middle_name": "",
    "last_name": "Doe"
}
```

### Employee List

```http
GET /api/employees/list/
```

### Delete Employee

```http
DELETE /api/employees/{employee_id}/
```

---

## API Response Format

Success Response

```json
{
    "success": true,
    "message": "Operation successful",
    "data": {}
}
```

Validation Error

```json
{
    "success": false,
    "message": "Validation failed",
    "errors": {}
}
```

Server Error

```json
{
    "success": false,
    "message": "Internal server error"
}
```

---

## License

This project is licensed under the MIT License.

---

