from flask import Flask, flash, url_for, render_template, request, session, redirect
from model.SignUpForm import SignUpForm
from model.LoginForm import LoginForm
from flask_login import LoginManager, login_user
from database import create_app
from model.Model import User, db
app = create_app()
# May need to specify password like this mysql://user:pass@localhost/tmi
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/tmi'
app.secret_key = 'development-key'
app.debug = True

loginManager = LoginManager()
loginManager.init_app(app)



@loginManager.user_loader
def load_user(userID):
    return User.query.filter(User.userID==userID).first()


@app.route('/', methods=['GET','POST'])
def index():
    login = LoginForm()
    if request.method == 'GET':
        return render_template('index.html', title='Welcome', login=login)

    elif request.method == 'POST':
        if login.validate():
            return 'Login Succesful'
        else:
            print('here')
            return render_template('login.html',title ='Sign In', login=login)
        


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    login = LoginForm()
    form = SignUpForm()
    if request.method == 'GET':
        return render_template('signup.html', title='Sign Up', form=form,login=login)
    elif request.method == 'POST':
        if form.validate():
            user = User(form.username.data,
                        form.password.data,
                        form.lastname.data,
                        form.firstname.data,
                        form.email.data,
                        form.address.data,
                        form.city.data,
                        form.state.data,
                        0,
                        'user')
            db.session.add(user)
            db.session.commit()
            return render_template('index.html',login=login)

        else:
            return render_template('signup.html',form=form, login=login)

@app.route('/login', methods=['GET','POST'])
def login():
    login = LoginForm()
    if request.method == 'GET':
        return render_template('login.html',login=login)
    elif request.method== 'POST':
        if login.validate():
            flash('Login Succesful')
            user = load_user(login.userID.data)
            if user.check_passwd(login.password.data):
                login_user(user)
                return redirect(url_for('index'))

            else:
                return 'Login Failed'
        else:
            return render_template('login.html', login=login)

if __name__ == '__main__':
    app.run()
