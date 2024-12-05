from market import app
from flask import render_template
from market.models import Item
from market import db
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')
@app.route('/market')
def market_page():
     items =Item.query.all()
     return render_template('market.html',items=items)
 # Add the shell context processor
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Item': Item}
