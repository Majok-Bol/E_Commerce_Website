'''Import flask class from Flask module'''
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
'''Create instance of flask class'''
app=Flask(__name__)
#configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
#create instance of database
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(length=30),nullable=False,unique=True)
    price=db.Column(db.Integer(),nullable=False)
    barcode=db.Column(db.String(length=12),nullable=False,unique=True)
    description=db.Column(db.String(length=1000),nullable=False,unique=True)
    def __repr__(self):
        return f"Item:{self.name}"
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

if __name__=='__main__':
    app.run(debug=True)