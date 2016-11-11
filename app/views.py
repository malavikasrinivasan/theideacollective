from flask import render_template, redirect, request, session, url_for, escape
from app import app, models, db
from .forms import LoginForm
# Access the models file to use SQL functions


@app.route('/')
def index():
    username = ''
    if 'username' in session:
        username = session['username']
        # trips = models.get_trips(username)
        return render_template('ideafeed.html', name=username)
    else:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/editprofile', methods=['GET', 'POST'])
def editprofile():
    pass

@app.route('/ideafeed', methods=['GET', 'POST'])
def ideafeed():
    return render_template('ideafeed.html')

@app.route('/ideapage', methods=['GET', 'POST'])
def ideapage():
    pass

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    pass

@app.route('/createidea', methods=['GET', 'POST'])
def createidea():
    pass

