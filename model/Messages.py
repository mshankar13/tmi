from database import db

class Message(db.Model):
    __tablename__='Message'

    MessageId = db.Column(db.INT, primary_key=True)
    MDate = db.Column(db.DATETIME)
    MSubject = db.Column(db.VARCHAR(100))
    MContent = db.Column(db.TEXT)
    MSenderId = db.Column(db.CHAR(14), db.ForeignKey('User.userID'))
    MReceiverId = db.Column(db.CHAR(14), db.ForeignKey('User.userID'))

    def __init__(self,mid,mdate,msub,mcont,sendid,recvid):
        self.MessageId=mid
        self.MDate=mdate
        self.MSubject = msub
        self.MContent = mcont
        self.MSenderId = sendid
        self.MReceiverId = recvid
