from flask import Flask, request
from utils.functions import select_query
from db.config import session
from db.models import Users

app = Flask(__name__)

@app.route("/")
def main():
    return {'message': 'Hello world'}

@app.route("/new/user", methods = ['POST'])
def newUser():
    try:
        name = request.json['name']
        fullname = request.json['fullname']
        password = request.json['password']
        isadmin = request.json['isadmin']

        user = Users(
            Username=name,
            Fullname=fullname,
            Password=password,
            IsAdmin=isadmin
        )

        session.add(user)
        session.commit
        
        return {
            'error': False,
            'message': f'User {name} creado exitosamente'
        }
    except Exception as e:
        
        return {
                'error': True,
                'message': e
            }

@app.route("/user", methods = ['GET'])
def getUser():

    users = select_query('Users')

    return {
        'error': False
    }

if __name__ == '__main__':
    app.run(debug=True)