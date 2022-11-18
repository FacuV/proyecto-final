from flask import Flask, render_template, request
import re
from db.config import get_db_connection
from utils.functions import create_user, logIn

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('signin.html')

@app.route("/signup", methods = ['POST'])
def newUser():
    cur, conn  = get_db_connection()
    try:
        with conn:
            username = request.form['username']
            fullname = request.form['fullname']
            password = request.form['password']


            if len(username) < 4:
                 raise Exception("El nombre de usuario debe tener una longitud mayor a 4 caracteres")
            if not re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
                 raise Exception("La contraseña no cumple los requisitos")
            
            if username and fullname and password:
                user = username, fullname, password, 0

                create_user(conn, cur, user)

                return render_template('users.html')
            else:
                raise Exception("Debes ingresar todos los campos")
    except Exception:
        return {
            'error': True,
            'message': f'Algo salió mal'
        }

@app.route("/login", methods = ['POST'])
def login():
    cur, conn  = get_db_connection()
    # try:
    with conn:
        username = request.form['username']
        password = request.form['password']

        response = logIn(conn, cur, username, password)
        return {
            'error': False,
            'message': response
        }

    # except Exception:
    #     return {
    #         'error': True,
    #         'message': f'Algo salió mal'
    #     }

@app.route("/users")
def getUsers():
    cur, conn  = get_db_connection()
    users = cur.execute('SELECT * FROM Users')
    return render_template('users.html', users=users)



@app.route("/search")
def searchImages():
    return render_template('finder.html')

if __name__ == '__main__':
    app.run(debug=True)