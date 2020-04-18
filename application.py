from flask import Flask
from flask import render_template, request, make_response
from markupsafe import escape

app = Flask(__name__)

BIG_SECRET = "THIS IS A BIG SECRET"

@app.route('/')
def index():
    if request.cookies.get('secret') == BIG_SECRET:
        return hello('old friend')
    return login()

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/login_submit/', methods=['POST'])
def login_submit():
    if valid_login(request.form['fname'],
                   request.form['fpassword']):
        resp = make_response(hello(request.form['fname']))
        resp.set_cookie('secret', BIG_SECRET)
        return resp
    else:
        return login() 

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

def valid_login(username, password):
    return username == "Alvin"
