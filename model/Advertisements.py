from database import db

class Advertisements(db.Model):
    __tablename__ = 'Advertisements'
    AdvertisementID = db.Column(db.INT, primary_key=True, autoincrement=True)
    EmployeeID = db.Column(db.INT, db.ForeignKey('Employee.UserID'))
    MerchandiseType = db.Column(db.CHAR(50))
    Company = db.Column(db.CHAR(50))
    ItemName = db.Column(db.CHAR(70))
    UnitPrice = db.Column(db.REAL)
    NoAvailableUnits = db.Column(db.INT)

    def __init__(self, eid,mt, co, iname, uprice, nounits):
        self.EmployeeID = eid
        self.MerchandiseType = mt
        self.Company = co
        self.ItemName = iname
        self.UnitPrice = uprice
        self.NoAvailableUnite = nounits