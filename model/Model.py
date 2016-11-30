from database import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tablename__ = 'User'
    userID = db.Column(db.CHAR(14),primary_key = True)
    passwd = db.Column(db.VARCHAR(54))
    lastName = db.Column(db.String(15))
    firstName = db.Column(db.String(15))
    email = db.Column(db.String(25))
    address = db.Column(db.String(25))
    city = db.Column(db.String(25))
    state = db.Column(db.String(25))
    rating = db.Column(db.REAL)
    userType = db.Column(db.String(15))

    def __init__(self,uid,pwd,fname,lname,email,address,city,state,rating,type):
        self.userID = uid
        self.passwd = generate_password_hash(pwd)
        self.lastName = lname
        self.firstName= fname
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.rating = rating
        self.userType =type

    def check_passwd(self,passwd):
        return check_password_hash(self.passwd,passwd)

    def get_id(self):
        return self.userID
