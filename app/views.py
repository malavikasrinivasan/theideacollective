from flask import render_template, redirect, request, session, url_for, escape
from app import app, models, db
from .forms import LoginForm, ProfileForm, IdeaForm, CommentForm
from .models import *
# Access the models file to use SQL functions


@app.route('/')
def index():
    if 'email' in session:
        email = escape(session['email'])
        # return render_template('editprofile.html', email=email, user_id=session['user_id'])
        return redirect('/editprofile')
    else:
        return redirect('/login')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method=='POST':
        email = request.form.get("email")
        password = request.form.get("password")
        session['user_id'] = 9999
        session['password'] = password
        session['email'] = email
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('password', None)
    session.pop('email', None)
    return redirect(url_for('index'))

@app.route('/editprofile', methods=['GET', 'POST'])
def editprofile():
    form = ProfileForm()
    if request.method=='POST':
        name = request.form.get("name")
        email = request.form.get("email")
        code = '123' + name
        bio = request.form.get("bio")
        add_user_profile(name, email, code, bio)
        return redirect('/login')
    return render_template('editprofile.html', form=form)

@app.route('/ideafeed', methods=['GET', 'POST'])
def ideafeed():
    return render_template('ideafeed.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    pass


@app.route('/createidea', methods=['GET', 'POST'])
def createidea():
    form = IdeaForm()
    return render_template('createidea.html', form=form)

@app.route('/ideapage/<idea_id>', methods=['GET', 'POST'])
def ideapage(idea_id):
    idea = get_idea(idea_id)
    # idea_dict = {} # Dictionary of users and passwords
    # idea_dict_keyList = ['id', 'idea_name', 'username', 'desc']
    # for idx, ida in enumerate(idea):
    #     idea_dict[idea_dict_keyList[idx]] = idea[idx]  
    # print(idea_dict)
    print(idea)
    # return render_template('ideapage.html', idea_detail=idea_dict)
    return render_template('ideapage.html', idea_detail=idea)
