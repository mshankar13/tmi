from flask import Flask, url_for, render_template, request
from flask_sessions import sessions
from model.SignUpForm import SignUpForm
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:localhost'
app.secret_key = 'dev-key'

@app.route('/')
def index():
    return render_template('index.html', title='Welcome')
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method =='GET':
        form = SignUpForm()
        return render_template('signup.html', title='Sign Up', form=form)
if __name__ == '__main__':
    app.run()

