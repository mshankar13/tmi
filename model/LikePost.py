from database import db
from model.Post import Post
from model.User import User

class LikePost(db.Model):
    __tablename__ = 'LikePost'
    PostId = db.Column(db.INT, db.ForeignKey('Post.postID'))
    UserId = db.Column(db.CHAR(14), db.ForeignKey('User.userID'))

    def __init__(self, pID, uID):
        self.PostId = pID
        self.UserId = uID