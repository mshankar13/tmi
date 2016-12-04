from database import db
from model.Group import Group

class Page(db.Model):
    __tablename__ = 'Page'
    pageID = db.Column(db.INT, primary_key=True,autoincrement=True )
    Powner = db.Column(db.CHAR(14))
    fGroup = db.Column(db.INT, db.ForeignKey('Group.groupID'))
    postCount = db.Column(db.INT)

    def __init__(self,pID,owner,group,postCount):
        self.pageID = pID
        self.Powner = owner
        self.fGroup = group
        self.postCount = postCount





