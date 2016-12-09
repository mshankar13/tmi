from database import db
from model.User import User

class Group(db.Model):
    __tablename__ = 'fGroup'
    groupID = db.Column(db.INT, primary_key=True, autoincrement=True)
    groupName = db.Column(db.VARCHAR(25))
    groupType = db.Column(db.VARCHAR(15))
    Gstatus = db.Column(db.VARCHAR(10))
    Gowner = db.Column(db.CHAR(14), db.ForeignKey('User.userID'))

    def __init__(self,gID,gname,gtype,gstatus,gowner):

        self.groupID=gID
        self.groupName = gname
        self.groupType = gtype
        self.Gstatus = gstatus
        self.Gowner = gowner

    @staticmethod
    def addUser(groupID, user):
        conn = db.engine.raw_connection()
        cursor = conn.cursor()
        cursor.callproc('joinGroup', args=[user.userID,'user',groupID])
        cursor.close()
        conn.commit()

