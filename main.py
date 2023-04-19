from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret = "this is a secret"
from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.utils import secure_filename


def getdb():
    engine = create_engine('sqlite:///project.sqlite')
    DBSession = sessionmaker(bind=engine)
    session = scoped_session(DBSession)
    return session

    


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup/add', methods=['GET', 'POST'])


def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        db = getdb()
        db.add(User(name=name,email=email,password=password))
        db.commit()
        db.close()
        return redirect('/signup/add')
    return render_template('signup.html')


@app.route('/login')
def login():
    if request.method == 'POST':
        email = request.form['Email']
        password = request.form['password']
        user = User.query.filter_by(email=username, password=password).first()
        if user is not None:
            session['logged_in'] = True
            session['username'] = username
            return redirect("/")
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')
 
    
@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect('/')
@app.route('/about')
def about():
    return render_template('about.html')





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
 