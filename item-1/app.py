from flask import Flask, render_template, request
from db.config import get_db_connection
from utils.functions import create_user

app = Flask(__name__)

@app.route("/")
def main():
    cur, conn = get_db_connection()
    users = cur.execute('SELECT * FROM Users')
    return render_template('signin.html')

@app.route("/new/user", methods = ['POST'])
def newUser():
    cur, conn  = get_db_connection()
    with conn:
        username = request.json['username']
        fullname = request.json['fullname']
        password = request.json['password']
        isadmin = request.json['isadmin']
        
        user = username, fullname, password, isadmin

        create_user(conn, cur, user)

        return render_template('signin.html' )

@app.route("/users", methods = ['GET'])
def allUsers():
    cur, conn = get_db_connection()
    users = cur.execute('SELECT * FROM Users')
    
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)