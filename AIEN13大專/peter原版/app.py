from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_sqlalchemy import SQLAlchemy  

app = Flask(__name__)
app.secret_key = 'any random string'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/members"

db = SQLAlchemy(app)                                                                  

class user(db.Model):
    UserID = db.Column(db.Integer, primary_key = True)
    UserName = db.Column(db.String(100), unique=True, nullable=False)
    UserPassword = db.Column(db.String(100), nullable=False)
    sex = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)

    def __init__(self, UserName, UserPassword, sex, birthday, height, weight):
        self.UserName = UserName
        self.UserPassword = UserPassword
        self.sex = sex
        self.birthday = birthday
        self.height = height
        self.weight = weight

@app.route('/')
def index():
    if 'UserName' in session:
        UserName = session['UserName']
        return render_template("index.html", page = 'member_center', pagename = '會員') 
    return render_template('index.html', page = 'login', pagename = '登入')

@app.route('/game')
def game():
    return render_template("game.html")

@app.route('/rank')
def rank():
    return render_template("rank.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        users = user.query.all()
        for person in users: 
            if request.form['usr'] == person.UserName and request.form['pwd'] == person.UserPassword: 
                session['UserName'] = request.form['usr']
                return redirect(url_for('index'))
                break
            error = 'Invalid username or password. Please try again!'   
    return render_template("login.html",  error = error)

@app.route('/logout')
def logout():
    session.pop('UserName', None)
    return redirect(url_for('index'))

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    # db.create_all()
    if request.method == 'POST':
        member = user(UserName = request.form['usr'], UserPassword = request.form['pwd'], sex = request.form['sex'], 
        birthday = request.form['bday'], height = request.form['height'], weight = request.form['weight'])
        db.session.add(member)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("signup.html")

@app.route('/member_center', methods = ['GET', 'POST'])
def membercenter():
    return render_template("member_center.html")

@app.route('/member_center/info', methods = ['GET', 'POST'])
def info():
    if request.method == 'POST':
        # 更新 database
        return redirect(url_for('membercenter'))
    return render_template("member_info.html")

if __name__ == '__main__':
   app.run(debug = True)