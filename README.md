#  Primetrade assignment Backend — FastAPI + PostgreSQL + Redis with flutter as frontend

The **Primetrade Backend** is a fully asynchronous REST API built with **FastAPI**, **SQLAlchemy (async)**, **PostgreSQL**, and **Redis caching**.  
It provides authentication (JWT), role-based routes, post creation, caching, and health checks — designed to be production-ready and easy to deploy.

This backend powers the Primetrade full-stack application.

---

## Features

### ✅ Authentication
- JWT-based login & signup  
- Password hashing with `passlib[bcrypt]`  
- Access token validation middleware  

### ✅ Posts API
- Create, update, delete posts  
- Get posts for authenticated users  
- Redis caching for fast reads  
- Automatic cache invalidation  

### ✅ Database Layer
- PostgreSQL with async SQLAlchemy engine  
- Alembic-friendly structure (optional)  
- Automatic initialization on startup  

### ✅ Health Checks
- `/health` endpoint verifies:
  - API status  
  - Database connectivity  

### ✅ Security
- Documentation disabled in production  

---

# run the backend

- `git clone https://github.com/AanishRahmani/primetrade_assignment.git`
- `cd primetrade_assignment`
- `cd primetrade_backend`
- `docker-compose up -d` 
- `pip install -r requirements.txt`
- `uv run main.py `
- `if you dont have uv use=> uvicorn app.app:app --host 0.0.0.0 --port ${PORT:-8000}`
- `go to http://127.0.0.1:8000/docs to test the api`

---

# setup the `.env` file

- JWT_SECRET_KEY=jwt-secret-key
- REDIS_URL = "redis://{inspect you docker container to get the redis ip and put it here}:6379"
- PORT=8080
