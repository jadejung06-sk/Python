from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
    
db.create_all()


## CREATE RECORD
new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# or (No primary key)
# new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
## READ RECORD
all_books = db.session.query(Book).all
## READ RECORD
book = Book.query.filter_by(title="Harry Potter").first()
## UPDATE RECORD
book_to_update = Book.query.filter_by(title='Harry Potter').first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()
# UPDATE RECORD
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()
# DELETE RECORD
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()


db.session.add(new_book)
db.session.commit()

##### sqlite3 case
# db = sqlite3.connect("./flask_backend/flask_SQLite_Database/books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


# all_books = [     

#     ]

# @app.route('/')
# def home():
#     return render_template('index.html', books=all_books)


# @app.route("/add", methods=['GET', 'POST'])
# def add():
#     if request.method == 'POST':
#         new_book = {
#             'title' : request.form['title'],
#             'author':request.form['author'],
#             'rating': request.form['rating']
#         }
#         all_books.append(new_book)
#         return redirect(url_for('home')) # 
#     return render_template('add.html')


# if __name__ == "__main__":
#     app.run(debug=True, use_reloader=False)

