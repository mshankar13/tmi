from database import db

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
    HourlyRate = db.Column(db.DOUBLE)
    CName = db.Column(db.CHAR(50))


def __init__(self,uid, usern, firstname, lastname, sdate, address, zipcode, state, telephone, hourlyrate, cname):
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


