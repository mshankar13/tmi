from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Welcome')
@app.route('/signup')
def signup():
    return render_template('signup.html', title='Sign Up')
if __name__ == '__main__':
    app.run()
