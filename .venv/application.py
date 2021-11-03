from flask import Flask
def create_app():
  app = Flask(__name__)

  @app.route('/')
  def index():
    return 'Hello World'
  return app
app = create_app()

@app.route('/books')
def get_books():
    return {"books": "books data "}



