# 📚 Book Review Blog

As an avid reader (and not a huge fan of having multiple social media accounts) this book review blog was developed with the goal to create a personal space where I can share my thoughts whenever I finish a book.

<br>

<p align="center">
  <img src="https://i.pinimg.com/originals/ff/cc/14/ffcc142948cb780c24c5e5086fd57016.gif" alt="open book flipping pages by itself">
</p>

<br>

## Technologies ⚙️
- Docker
- Flask
- PostgreSQL
- Python

## Project Structure

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
