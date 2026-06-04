from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from data_models import db, Author, Book
from datetime import datetime
import os


app = Flask(__name__)

app.secret_key = 'joséramos'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"


db.init_app(app)


@app.route('/add_author', methods=['GET','POST'])
def add_author():
    if request.method == 'POST':
        name = request.form.get('name')
        birthdate = request.form.get('birthdate')
        date_of_death = request.form.get('date_of_death')

        birthdate = datetime.strptime(birthdate,
                                       "%Y-%m-%d").date() if birthdate else None
        date_of_death = datetime.strptime(date_of_death,
                                          "%Y-%m-%d").date() if date_of_death else None

        author = Author(name=name, birth_date=birthdate, date_of_death=date_of_death)

        db.session.add(author)
        db.session.commit()

        return render_template('add_author.html', message='Author added with Success.')

    else:
        return render_template('add_author.html')


@app.route('/add_book', methods=['GET','POST'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        isbn = request.form.get('isbn')
        pub_year = request.form.get('pub_year')
        author_id = request.form.get('author_id')

        book = Book(title=title, isbn=isbn, publication_year=pub_year, author_id=author_id)

        db.session.add(book)
        db.session.commit()

        authors = Author.query.all()

        return render_template('add_book.html', authors=authors, message='Book added with Success')


    else:
        authors = Author.query.all()
        return render_template('add_book.html', authors=authors)


@app.route('/')
def home_page():
    sort = request.args.get('sort')
    search = request.args.get('search')

    if sort == 'title':
        books = Book.query.order_by(Book.title).all()

    elif sort == 'author':
        books = (Book.query.join(Author).order_by(Author.name).all())

    elif search:
        books = Book.query.filter(Book.title.ilike(f"%{search}%")).all()
        if len(books) == 0:
            flash('Book not found!')
            return render_template('home.html', books=books)

    else:
        books = Book.query.all()

    # books = (
    #     db.session.query(Book, Author)
    #     .join(Author, Book.author_id == Author.id)
    #     .all()
    # )
    # for book in books:
    #     print(book.isbn)

    return render_template('home.html', books=books)


@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    select_book = Book.query.get(book_id)
    if select_book is None:
        flash('Book not found')
        return redirect(url_for('home_page'))

    check_author = Book.query.filter_by(author_id=select_book.author_id).count()

    db.session.delete(select_book)

    if check_author == 1:
        select_author = Author.query.get(select_book.author_id)
        db.session.delete(select_author)

    db.session.commit()
    flash('Book deleted successfully!')
    return redirect(url_for('home_page'))


if __name__ == '__main__':
    app.run(debug=True, port=5002)