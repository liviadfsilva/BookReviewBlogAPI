# 📚 Book Review Blog

![Python](https://img.shields.io/badge/Python-3.13.2-yellow?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-3.1.1-white?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?style=for-the-badge)
![JWT](https://img.shields.io/badge/Jwt-Auth-green?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/Postgres-8.0-7AADFF?style=for-the-badge)
![Licence](https://img.shields.io/badge/Licence-MIT-pink?style=for-the-badge)

<br>

## About ✨

Book Review Blog is a RESTful API for managing users, books, reviews and personal blog posts, designed to support a complete book review and blogging platform.

<br/>

## Features ⚙️
- JWT Authentication
- Book Categorisation
- Rating and review system
- RESTful endpoints for CRUD operations

<br/>

## Installation 💻

1. **Clone the repository:**

   ```sh
   git clone https://github.com/liviadfsilva/BookReviewBlogAPI.git
   cd BookReviewBlogAPI
   ```

2. **Copy the .env.example file to .env and change the environment variables if necessary:**

   ```sh
   cp .env.example .env
   ```

3. **Build and start the application and database with Docker**

   ```bash
    docker compose up --build
   ```
<br/>

#### The application will start at:
꩜ **http://localhost:5001**

#### Access the Swagger documentation:
📜 **http://localhost:5001/docs/#/**

<br/>

## Project Structure 🧬

```
app
   |-- controllers
   |   |-- __init__.py
   |   |-- auth.py
   |   |-- posts.py
   |   |-- reviews.py
   |   |-- tags.py
   |   |-- user.py
   |-- models
   |   |-- __init__.py
   |   |-- base.py
   |   |-- db.py
   |   |-- post.py
   |   |-- review_tags.py
   |   |-- review.py
   |   |-- tag.py
   |   |-- user.py
   |-- schemas
   |   |-- __init__.py
   |   |-- post_schema.py
   |   |-- review_schema.py
   |   |-- tags_schema.py
   |   |-- user_schema.py
   |-- seeds
   |   |-- __init__.py
   |   |-- tags.py
   |   |-- run_seeds.py
   |-- static
   |   |-- swagger.json
   |-- __init__.py
   |-- initializer.py
   |-- server.js
migrations
  |-- versions
  |-- .env
  |-- alembic.ini
.env.example
.gitignore
.config.py
docker-compose.yml
Dockerfile
main.py
requirements.txt
```

<br/>

## Inspiration 📚

The idea behind this project was the desire of having a place of my own to make book reviews and blog posts without the need to have multiple social media accounts for that.

<br/>

## Future Improvements 🧩

- Add pagination to book reviews and blog posts

<br/>

## Author 🩷
**Lívia Silva**<br/>
Backend Developer

- GitHub: https://github.com/liviadfsilva 
- LinkedIn: https://linkedin.com/in/liviadfsilva

<br/>

## Licence 📋
This software is licenced under the MIT Licence.