from flask import request, redirect, render_template
from app import app
from models import *

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST','GET'])
def index():
    if request.method=='POST':
        insert_name= request.form['name']
        insert_email=request.form['email']
        
        new_User=User(name=insert_name , email=insert_email)

        try:
            db.session.add(new_User)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding the details of the User to your database'
    else:
        users = User.query.order_by(User.id).all()
        return render_template('generic.html', users=users)