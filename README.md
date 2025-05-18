
# Notification Service

A backend service built using **FastAPI** that enables sending notifications via **Email**, **SMS**, and **In-App** methods theough **PostgreSQL** database.

---

## Features

-  Send notifications via:
  -  Email
  -  SMS
  -  In-App
-  REST API with Swagger UI for testing

---

## Technologies Used

- **FastAPI** – Web framework
- **PostgreSQL** – Database
- **SQLAlchemy** – ORM for database models
- **Pydantic** – Data validation
- **Uvicorn** – ASGI server

---

## Prerequisites

Ensure the following are installed and working:

- Python 3.8+
- PostgreSQL
- Git (for local version control)

---

## Setup Instructions

### 1️.Clone the Project

```bash
git clone <your-repository-url>
cd notification-service
```

### 2️.Create a Virtual Environment

```bash
python -m venv venv
# Activate the environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3️.Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️.Configure Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/notifications
EMAIL_USER=your-email@example.com
EMAIL_PASS=your-email-password
TWILIO_SID=your_twilio_sid
TWILIO_AUTH=your_twilio_auth_token
TWILIO_PHONE=+1234567890
```

Replace placeholder values with your actual configuration.

---

## 5.Database Setup

Ensure PostgreSQL is running and a database named `notifications` is created:

```sql
CREATE DATABASE notifications;
```

Then, run the following Python command to create tables:

```bash
python -c "from app import models, database; models.Base.metadata.create_all(bind=database.engine)"
```

---

## Run the Notification Service

### 1. Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

Access Swagger UI at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Using the API

### Send Notification

**POST /notifications**

**Body Example:**
```json
{
  "user_id": 1,
  "message": "Welcome to our service!",
  "type": "email"
}
```

### Fetch Notification Logs

**GET /users/{user_id}/notifications**

Replace `{user_id}` with the target user ID to get their message history.

---

## 🛠️ Troubleshooting

| Issue                            | Solution                                                  |
|----------------------------------|-----------------------------------------------------------|
| `DATABASE_URL` error             | Check .env file & PostgreSQL service                     |
| Notifications not sending        | Verify email/SMS config in `.env`                        |
| Tables not found                 | Run `Base.metadata.create_all(...)` as shown above       |

---
