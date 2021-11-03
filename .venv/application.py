from flask import Flask
def create_app():
  app = Flask(__name__)
  return app
app = create_app()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.author} - {self.description}"

@app.route('/books')
def get_books():
    return {"books": "books data "}





