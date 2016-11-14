from flask import render_template, redirect, request, session, url_for, escape
from app import app, models, db
from .forms import LoginForm, ProfileForm, IdeaForm
# Access the models file to use SQL functions


# @app.route('/')
# def index():
#     username = ''
#     if 'username' in session:
#         username = session['username']
#         # trips = models.get_trips(username)
#         return render_template('ideafeed.html', name=username)
#     else:
# #         return redirect('/login')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     return render_template('login.html', form=form)

@app.route('/editprofile', methods=['GET', 'POST'])
def editprofile():
    form = ProfileForm()
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

@app.route('/ideapage', methods=['GET', 'POST'])
def ideapage():
    return render_template('ideapage.html') 


@app.route('/')
def index():
    # SEL
    if 'email' in session:
        email = escape(session['email'])
        # print(session['email'], session['password'], session['user_id'])
        return render_template('editprofile.html', email=email, user_id=session['user_id'])
        # SEL
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

# @app.route('/editprofile', methods=['GET', 'POST'])
# def editprofile():
#     form = ProfileForm()
#     return render_template('login.html', form=form)
# # SEL
