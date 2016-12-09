from database import db
from model.Advertisements import Advertisements

class Sales(db.Model):
    __tablename__ = 'Sales'
    TransactionID = db.Column(db.INT, primary_key=True)
    AdvertisementID = db.Column(db.INT, db.ForeignKey('Advertisements.AdvertisementID'))
    NumberofUnits = db.Column(db.INT)
    AccountNumber = db.Column(db.INT)
    UserID = db.Column(db.CHAR(14))

def __init__(self, tid, aid, nou, ano, uid):
    self.TransactionID = tid
    self.AdvertisementID = aid
    self.NumberofUnits = nou
    self.AccountNumber = ano
    self.UserID = uid
