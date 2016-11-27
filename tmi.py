from flask import Flask, url_for, render_template, request
from flask_sessions import sessions
from model.SignUpForm import SignUpForm
from model.Model import db, User
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:localhost/tmi'
app.secret_key = 'dev-key'

db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html', title='Welcome')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'GET':
        return render_template('signup.html', title='Sign Up', form=form)
    elif request.method == 'POST':
        if form.validate():
            user = User(form.username.data,
                        form.password.data,
                        form.firstname.data,
                        form.lastname.data,
                        form.email.data,
                        form.address.data,
                        form.city.data,
                        0,
                        'user')
            db.session.add(user)
            db.session.commit()

        else:
            print('here')

            return render_template('signup.html',form=form)



if __name__ == '__main__':
    db.create_all()
    app.run()
