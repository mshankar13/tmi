from database import db

class Member(db.Model):
    __tablename__ = 'Member'
    groupID = db.Column(db.INT, db.ForeignKey('fGroup.groupID') ,primary_key=True)
    membership = db.column(db.VARCHAR(10))
    userID = db.Column(db.CHAR(14), db.ForeignKey('User.userID'), primary_key=True)

    def __init__(self, groupID,membership,userID):
        self.groupID = groupID
        self.membership=membership
        self.userID = userID




