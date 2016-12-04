from database import db
from model.Page import Page
from model.User import User

class Post(db.Model):
    __tablename__ = 'Post'
    postID = db.Column(db.INT, primary_key=True, autoincrement=True)
    owner = db.Column(db.CHAR(14), db.ForeignKey('User.userID'))
    pageID = db.Column(db.CHAR(14), db.ForeignKey('Page.pageID'))
    postDate = db.Column(db.DATETIME)
    content = db.Column(db.TEXT)
    commentCount = db.Column(db.INT)
    likesCount = db.Column(db.INT)

    def __init__(self,pid,owner,paid,pdate,content,ccount,lcount):
        self.postId = pid
        self.owner = owner
        self.pageID=paid
        self.postDate=pdate
        self.content = content
        self.commentCount = ccount
        self.likesCount = lcount
