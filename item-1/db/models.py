import sqlalchemy as db

class Users():
    Id = db.Column(db.Integer(), primary_key=True)
    Username = db.Column(db.String(50), primary_key=False)
    Fullname = db.Column(db.String(200), primary_key=False)
    Password = db.Column(db.String(120), primary_key=False)
    IsAdmin = db.Column(db.Integer(), primary_key=False)