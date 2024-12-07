from market import app
from flask import render_template
from market.models import Item
from market import db
from market.forms import RegisterForm
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')
@app.route('/market')
def market_page():
     items =Item.query.all()
     return render_template('market.html',items=items)
 #create router for registering form
@app.route('/register')
def register_page():
     #use register form class to create instance of form
     form=RegisterForm()
     #send users to register.html, send information to that template,ie the form instance 
     return render_template('register.html',form=form)
     
 # Add the shell context processor
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Item': Item}
