from flask import Flask, render_template, request, redirect, url_for
import re
from db.config import get_db_connection
from utils.functions import create_user, logIn, getColumns, albumAndArtist
from pprint import pprint

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

                return redirect('/users')
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
    with conn:
        username = request.form['username']
        password = request.form['password']

        user = logIn(conn, cur, username, password)
        isLogged = True if user else False

        if isLogged:
            return redirect('/search')
        else:
            return render_template('signin.html')

@app.route("/users")
def getUsers():
    cur, conn  = get_db_connection()
    users = cur.execute('SELECT * FROM Users')
    return render_template('users.html', users=users)



@app.route("/search")
def searchImages():
    cur, conn  = get_db_connection()
    album = albumAndArtist(conn, cur)
    myList = []
    for artist in album:
        data = ('id', 'album', 'artist')
        if len(artist) == len(data):
            res = {data[i] : artist[i] for i, _ in enumerate(artist)}
            myList.append(res)

    return render_template('finder.html', myList=myList)

if __name__ == '__main__':
    app.run(debug=True)