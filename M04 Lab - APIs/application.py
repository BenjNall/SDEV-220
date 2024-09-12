#Program Name: application.py
#Author: Ben Nall
#Date 9/11/2024
#Purpose: To create a simple API using Flask and SQLAlchemy that creates a DB holding books

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# define books class with id, name, and description
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f"{self.name} - {self.description}"
    

#route for the API to return a simple hello world
@app.route('/')
def index():
    return "Hello, World!"

#route to get all books
@app.route('/books')
def get_drinks():
    books = Book.query.all()

#builds an object and adds each book 1 by 1
    output = []
    for book in books:
        book_data = {'name': book.name, 'description': book.description}
        output.append(book_data)
    return {'books': output}

#route to get a specific book by id
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'name': book.name, 'description': book.description}

#route to add a book
@app.route('/books', methods=['POST'])
def add_book():
    book = Book(name=request.json['name'], description=request.json['description'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

#route to delete a book
@app.route('/books/<id>', methods=['DELETE'])
def delete_book():
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "success"}