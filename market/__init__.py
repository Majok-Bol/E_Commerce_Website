'''Import flask class from Flask module'''
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
'''Create instance of flask class'''
app=Flask(__name__)
#configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# app.config['SECRET_KEY']='b98a2a87bcdfd3d9686f6892'
db = SQLAlchemy(app)
#create instance of database

from market import routes

