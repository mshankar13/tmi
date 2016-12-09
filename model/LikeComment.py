from database import db
from model.Comment import Comment
from model.User import User

class LikeComment(db.Model):
    __tablename__ = 'LikeComment'
    CommentId = db.Column(db.INT, db.ForeignKey('Comment.commentID'))
    UserId = db.Column(db.CHAR(14), db.ForeignKey('User.userID'))

    def __init__(self, cID, uID):
        self.CommentId = cID
        self.UserId = uID