from database import db
from model.Post import Post
from model.User import User

class Comment(db.Model):
    __tablename__ = 'Comment'
    commentID = db.Column(db.INT, primary_key=True, autoincrement=True)
    postID = db.Column(db.INT, db.ForeignKey('Post.postID'))
    created = db.Column(db.DATE)
    content = db.Column(db.TEXT)
    author = db.Column(db.CHAR(14), db.ForeignKey('User.userID'))
    likesCount = db.Column(db.INT)

    def __init__(self, coID, poID, cre, con, aut, lCnt):
        self.commentID = coID
        self.postID = poID
        self.created = cre
        self.content = con
        self.author = aut
        self.author = lCnt