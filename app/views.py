from flask import render_template,  request, redirect, url_for
from app.database import db, Book

def index_page():
    return render_template("index.html")
def book_list():
    query = db.select(Book)
    books = db.session.execute(query).scalars()
    return render_template("book_list.html", books=books)
def book_edit():
    book = Book()
    if request.method == 'POST':
        book.name = request.form["name"]
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("book_list"))
    return render_template("book_edit.html")