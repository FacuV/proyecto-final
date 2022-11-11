from flask import Flask
from db.config import session, engine
from db.models import Users

app = Flask(__name__)

@app.route("/")
def main():
    return {'message': 'Hello world'}

if __name__ == '__main__':
    app.run(debug=True)