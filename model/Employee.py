from database import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class Employee(db.Model):
    __tablename__ = 'Employee'
    SSN = db.Column(db.INT,primary_key=True)
    UserId = db.Column(db.CHAR(14))
    FirstName = db.Column(db.CHAR(50))
    LastName = db.Column(db.CHAR(50))
    StartDate = db.Column(db.DATE)
    Address = db.Column(db.CHAR(70))
    ZipCode = db.Column(db.INT)
    State = db.Column(db.CHAR(50))
    Telephone = db.Column(db.INT)
    HourlyRate = db.Column(db.INT)
    CName = db.Column(db.CHAR(50))

    def __init__(self, uid, usern, firstname, lastname, sdate, address, zipcode, state, telephone, hourlyrate, cname):
        self.SSN = uid
        self.UserId = usern
        self.FirstName = firstname
        self.LastName = lastname
        self.StartDate = sdate
        self.Address = address
        self.ZipCode = zipcode
        self.State = state
        self.Telephone = telephone
        self.HourlyRate = hourlyrate
        self.CName = cname

    @staticmethod
    def addEmployee(form):
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        s = generate_password_hash(form.password.data)
        cursor.callproc('AddEmployee', [form.socialsecurity.data,
                                         form.username.data,
                                         form.firstname.data,
                                         form.lastname.data,
                                         form.address.data,
                                         form.zipcode.data,
                                         form.state.data,
                                         form.telephone.data,
                                         form.hourlypay.data,
                                         form.company.data,
                                         s,
                                         form.city.data,
                                         form.email.data])
        cursor.close()
        connection.commit()





