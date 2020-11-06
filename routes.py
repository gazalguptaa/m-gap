from flask import request, redirect, render_template
from app import app
from models import *

@app.route('/')
def home():
    return render_template('index.html')

import utils

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/verify')
def verify():
    return render_template('verify.html')

@app.route('/send_details', methods=['POST','GET'])
def index():
    if request.method=='POST':
        name= request.form['demo-name']
        email=request.form['demo-email']
        gender=request.form['demo-gender']
        age = request.form['demo-age']
        contact = request.form['demo-contact']
        
        new_User=User(name=name, email=email, gender=gender, age=age, contact=contact)

        try:
            db.session.add(new_User)
            db.session.commit()
            return redirect('/register')
        except Exception as e:
            print(e)
            return 'There was an issue adding the details of the User to your database'
    else:
        users = User.query.order_by(User.id).all()
        return render_template('register.html', users=users)

@app.route('/verification_details', methods=['POST','GET'])
def details():
    if request.method=='POST':
        temperature= request.form['demo-temp']
        new_Scan=Scan(temperature=temperature)

        try:
            db.session.add(new_Scan)
            db.session.commit()
            return redirect('/verify')
        except:
            return 'There was an issue adding the details of the User to your database'
    else:
        details = Scan.query.order_by(Scan.id).all()
        return render_template('verify.html', details=details)

@app.route('/register-image', methods=['POST'])
def register_face():
    image = request.files['webcam']
    


