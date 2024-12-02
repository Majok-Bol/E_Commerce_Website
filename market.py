'''Import flask class from Flask module'''
from flask import Flask
'''Create instance of flask class'''
app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'

if __name__=='__main__':
   app.run()