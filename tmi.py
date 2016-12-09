from flask import Flask, url_for, render_template, request, redirect
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from Data.LoginForm import LoginForm
from Data.PostForm import PostForm
from Data.SearchForm import SearchForm
from Data.SignUpForm import SignUpForm
from Data.GroupForm import GroupForm
from Data.MessageForm import MessageForm
from Data.AddEmployeeForm import AddEmployeeForm
from Data.RemoveEmployeeForm import RemoveEmployeeForm
from database import create_app
from model.User import User, db
from model.Page import Page
from model.Post import Post
from model.Messages import Message
from model.Group import Group
from model.Employee import Employee
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
        if current_user.userType == 'manager':
            return redirect(url_for('manager'))
        elif current_user.userType == 'user':
            return redirect(url_for('home'))
        elif current_user.userType == 'employee':
            return redirect(url_for('employee'))
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
            # If user adds posts and the fields in the form valid then add post to database
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.callproc('ownerMakePost', [current_user.userID, makepost.post.data])
            cursor.close()
            connection.commit()
        else:
            return render_template('home.html', posts=posts, formpost=makepost, searchForm=search)
        return redirect(url_for('home'))



#================================== MANAGER / USER TRANSACTIONS AND METHODS ======================================== #

# Manager Home Page
@app.route('/manager')
@login_required
def manager():
    return render_template('manager.html')

# Employee Home Page
@app.route('/employee')
@login_required
def employee():
    return render_template('employee.html')

# add_employee method
@app.route('/addEmployee', methods=['GET', 'POST'])
@login_required
def add_employee():
    login = LoginForm()
    form = AddEmployeeForm()
    if request.method == 'GET':
        return render_template('addEmployee.html', title='Add Employee', form=form, login=login)
    elif request.method == 'POST':
        if form.validate():
            Employee.addEmployee(form)
            return redirect(url_for('displayEmployees'))
        else:
            return render_template('addEmployee.html', title='Add Employee', form=form, login=login)


# remove employee
@app.route('/removeEmployee', methods=['GET', 'POST'])
@login_required
def remove_employee():
    login = LoginForm()
    form = RemoveEmployeeForm()
    if request.method == 'GET':
        return render_template('removeEmployee.html',title='Remove Employee', form=form, login=login)
    elif request.method == 'POST':
        if form.validate():
            Employee.removeEmployee(form)
            return redirect(url_for('displayEmployees'))
        else:
            return render_template('removeEmployee.html', title='Remove Employee', form=form, login=login)

# edit employee


# Obtain Sales Report
@app.route('/salesReportMonth', methods =['GET','POST'])
@login_required
def salesReportMonth():
    if request.method == 'POST':
        return render_template('salesReportMonth.html')
    elif request.method == 'GET':
        return render_template('salesReportMonth.html')


# Obtain advertised list
@app.route('/salesReportMonth', methods =['GET','POST'])
@login_required
def advertisedList():
    if request.method == 'POST':
        return render_template('displayAdvertisedList.html')
    elif request.method == 'GET':
        return render_template('displayAdvertisedList.html')


# List of Transaction By ItemName

# List of Transactions By UserName

# List of Customers Who purchased a particular item

# List items being sold for a given company


# Record a transaction


# Create Advertisement
@app.route('/createAdvertisement',methods=['GET','POST'])
@login_required
def createAdvertisement():
    if request.method == 'POST':
        return render_template('createAdvertisement.html')
    elif request.method == 'GET':
        return render_template('createAdvertisement.html')


# Remove Advertisement






# Display all Employees in the Employee Table
@app.route('/displayEmployees')
@login_required
def displayEmployees():
        employees = Employee.query.all()
        return render_template('displayEmployees.html',employees=employees)







# ==================================== END MANAGER/EMPLOYEE TRANSACTIONS ===================================#

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
            return redirect(url_for('groups', groupName=groupForm.name.data, groups=groups))
        else:
            return render_template('groups.html', groupForm=groupForm, searchform=search)


@app.route('/groups/<int:groupID>', methods=['GET', 'POST'])
def groups(groupID):
    if request.method=='GET':
        search = SearchForm()
        makePost = PostForm()
        page=Page.query.filter(Page.fGroup==groupID).first()
        posts= Post.query.filter(Post.pageID==page.pageID).order_by(Post.postDate.desc()).all()
        return render_template('group_page.html', searchform=search, formpost=makePost,posts=posts)


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
