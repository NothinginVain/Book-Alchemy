from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    """
    Database model representing a book author.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.Date)
    date_of_death = db.Column(db.Date)

    def __str__(self):
        """
        Return the author's name.
        """
        return self.name


class Book(db.Model):
    """
    Database model representing a book.
    """

    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, unique=True)
    title = db.Column(db.String, nullable=False)
    publication_year = db.Column(db.Integer)

    author_id = db.Column(
        db.Integer,
        db.ForeignKey('author.id'),
        nullable=False
    )
    author = db.relationship('Author')

    def __str__(self):
        """
        Return the book title.
        """
        return self.title