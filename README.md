# Book Alchemy

Flask web application for managing a small library of books and authors. Users can add authors, add books, search the library, sort by title or author, and delete books while preserving the relationship between books and authors.

## Features

- Add authors with birth and death dates
- Add books connected to existing authors
- Search books by title
- Sort books by title or author
- Delete books from the library
- Automatically remove authors when their last book is deleted
- Flash messages for user feedback
- SQLite database using SQLAlchemy models

## Tech Stack

Python · Flask · Flask-SQLAlchemy · SQLite · HTML · CSS · Jinja2

## Getting Started

```bash
git clone https://github.com/NothinginVain/Book-Alchemy.git
cd Book-Alchemy
python -m venv .venv
source .venv/bin/activate
pip install flask flask-sqlalchemy
python app.py
```

The app runs locally as a Flask development server.

## What This Project Demonstrates

- Flask routing and templates
- SQLAlchemy model relationships
- Form handling
- Search and sorting
- Basic database-driven web app structure

## Security Note

The Flask `SECRET_KEY` should be loaded from an environment variable instead of being hardcoded in the repository.

