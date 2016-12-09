from flask import Flask, url_for, render_template, request, redirect
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from Data.LoginForm import LoginForm
from Data.PostForm import PostForm
from Data.SearchForm import SearchForm
from Data.SignUpForm import SignUpForm
from Data.GroupForm import GroupForm
from Data.MessageForm import MessageForm
from database import create_app
from model.User import User, db
from model.Page import Page
from model.Post import Post
from model.Messages import Message
from model.Group import Group
from model.Member import Member
from model.Comment import Comment
from os import environ

app = Flask(__name__)
# May need to specify password like this mysql://user:pass@localhost/tmi
address = 'mysql://%s:%s@localhost/tmi' % (environ['DBUSER'], environ['DBPASS'])
app.config['SQLALCHEMY_DATABASE_URI'] = address
app.secret_key = 'development-key'
app.debug = True

loginManager = LoginManager()
loginManager.init_app(app)


@loginManager.user_loader
def load_user(userID):
    return User.query.filter(User.userID == userID).first()


# Index page
@app.route('/', methods=['GET'])
def index():
    login = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'GET':
        return render_template('index.html', title='Welcome', login=login)


# User Home page
@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    search = SearchForm()
    makepost = PostForm()
    userID = current_user.userID
    page = Page.query.filter(Page.Powner == userID).first()
    posts = Post.query.filter(Post.pageID == page.pageID).order_by(Post.postDate.desc())

    if request.method == 'GET':
        return render_template('home.html', posts=posts, formpost=makepost, searchform=search)
    elif request.method == 'POST':
        if makepost.validate():
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.callproc('ownerMakePost', [current_user.userID, makepost.post.data])
            cursor.close()
            connection.commit()
        else:
            return render_template('home.html', posts=posts, formpost=makepost, searchForm=search)
        return redirect(url_for('home'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


# signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    login = LoginForm()
    form = SignUpForm()
    if request.method == 'GET':
        return render_template('signup.html', title='Sign Up', form=form, login=login)
    elif request.method == 'POST':
        if form.validate():
            User.registerUser(form)
            return render_template('index.html', login=login)

        else:
            return render_template('signup.html', form=form, login=login)


# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    login = LoginForm()
    if request.method == 'GET':
        return render_template('home.html', login=login)
    elif request.method == 'POST':
        return signinUser(login)


# search users
@app.route('/search', methods=['POST'])
@login_required
def search():
    search = SearchForm()
    if request.form['search']:
        users = User.query.filter(User.userID.like(request.form['search'])).all()
    else:
        users = User.query.all()
    return render_template('Users.html', users=users, searchform=search)


# send message

@app.route('/message/<username>', methods=['POST', 'GET'])
@login_required
def message(username):
    search = SearchForm()

    messages = Message.query.filter(
        db.or_(db.and_(Message.MSenderId == current_user.userID, Message.MReceiverId == username), \
               db.and_(Message.MReceiverId == current_user.userID, Message.MSenderId == username))) \
        .order_by(Message.MSubject, Message.MDate).all()

    message = MessageForm()
    if request.method == 'GET':
        return render_template('message.html', user=username, message=message, messages=messages, searchform=search)

    if request.method == 'POST':
        if message.validate():
            conn = db.engine.raw_connection()
            cursor = conn.cursor()
            cursor.callproc('SendMessage',
                            args=[message.subject.data, message.content.data, current_user.userID, username])
            cursor.close()
            conn.commit()
            return redirect(url_for('message', username=username))
        else:
            return render_template('message.html', user=username, searchform=search, message=message, messages=messages)
def is_admin():
    return current_user.userType == 'manager'

@app.route('/group', methods=['GET', 'POST'])
@login_required
def group():
    groupForm = GroupForm()
    search = SearchForm()
    groups = Group.query.all()
    if request.method == 'GET':
        return render_template('groups.html', searchform=search, groupForm=groupForm, groups=groups)
    if request.method == 'POST':
        if groupForm.validate():
            conn = db.engine.raw_connection()
            cursor = conn.cursor()
            cursor.callproc('createGroup',
                            args=[groupForm.name.data, 'organization',
                                  'public', current_user.userID])
            cursor.execute('SELECT @groupID')
            groupID = cursor.fetchone()
            cursor.close()
            conn.commit()
            return redirect(url_for('groups', groupID=groupID[0]))
        else:
            return render_template('groups.html', groupForm=groupForm, searchform=search)

@app.route('/groups/<int:groupID>', methods=['GET', 'POST'])
def groups(groupID):

    makePost = PostForm()
    search = SearchForm()
    page = Page.query.filter(Page.fGroup == groupID).first()
    posts = Post.query.filter(Post.pageID == page.pageID).order_by(Post.postDate.desc())
    comments = Comment.query.filter(Comment.postID.in_(db.session.query(Post.postID).filter(Post.pageID==page.pageID))).all()
    members = db.session.query(User, Member).filter(User.userID == Member.userID, Member.groupID == groupID).all()
    if request.method=='GET':
        posts= Post.query.filter(Post.pageID==page.pageID).order_by(Post.postDate.desc()).all()
        return render_template('group_page.html', comments=comments, searchform=search, formpost=makePost,posts=posts,members=members,groupID=groupID)
    elif request.method == 'POST':
        userID = current_user.userID
        if makePost.validate():
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.callproc('postOnGroup', [current_user.userID, groupID, makePost.post.data])
            cursor.close()
            connection.commit()
        else:
            return render_template('group_page.html', posts=posts, formpost=makePost, searchform=search, members=members, groupID=groupID)
        return redirect(url_for('groups', groupID=groupID))

@app.route('/join/<int:groupID>')
def join(groupID):
    Group.addUser(groupID,current_user)
    return redirect(url_for('groups', groupID=groupID))

@app.route('/groups/<int:groupID>/users')
def group_users():
    pass

@app.route('/groups/<int:groupID>/<int:postID>', methods=['POST'])
def make_comment(groupID,postID):
    conn = db.engine.raw_connection()
    cursor = conn.cursor()
    cursor.callproc('commentOnGroup', args=[postID,request.form['comment'],current_user.userID])
    cursor.close()
    conn.commit()
    return redirect(url_for('groups',groupID=groupID))

@app.route('/groups/<int:groupID>/<int:postID>/del/<int:commentID>', methods=['GET'])
def delete_comment(groupID,postID,commentID):
    Comment.query.filter(Comment.commentID == commentID).delete()
    db.session.commit()
    return redirect(url_for('groups', groupID=groupID))

@app.route('/groups/<int:groupID>/del/<int:postID>', methods=['GET'])
def delete_post(groupID, postID):
    Post.query.filter(Post.postID == postID).delete()
    db.session.commit()
    return redirect(url_for('groups', groupID=groupID))

def signinUser(login):
    if login.validate():
        user = load_user(login.userID.data)
        if user.check_passwd(login.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            return 'Login Failed'
    else:
        print(login.errors)
        return render_template('login.html', login=login)


if __name__ == '__main__':
    create_app(app)
    app.run()
