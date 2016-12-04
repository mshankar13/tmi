from flask import Flask, url_for, render_template, request, redirect
from flask_login import LoginManager, login_user, current_user, logout_user
from Data.LoginForm import LoginForm
from Data.PostForm import PostForm

from Data.SignUpForm import SignUpForm
from database import create_app
from model.User import User, db
from model.Page import Page
from model.Post import Post

app = Flask(__name__)
# May need to specify password like this mysql://user:pass@localhost/tmi
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Trevor24@localhost/tmi'
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
def home():
    makepost = PostForm()
    userID = current_user.userID
    page = Page.query.filter(Page.Powner==userID).first()
    posts = Post.query.filter(Post.pageID == page.pageID).order_by(Post.postDate.desc())


    if request.method == 'GET':
        return render_template('home.html', posts=posts, formpost=makepost)
    elif request.method == 'POST':
        if makepost.validate():
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.callproc('ownerMakePost',[current_user.userID, makepost.post.data])
            cursor.close()
            connection.commit()
        else:
            return render_template('home.html',posts=posts, formpost=makepost)
        return redirect(url_for('home'))



@app.route('/logout')
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
