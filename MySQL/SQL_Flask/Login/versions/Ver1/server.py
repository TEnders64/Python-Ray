 # Login and Registration
# Version 1 with basic routing
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'Godzilla'
mysql = MySQLConnector(app,'mydb')

# index
@app.route('/', methods=['GET'])
def index():
    if 'loginid' not in session:
        session['loginid'] = 0
    if 'registered' not in session:
        session['registered'] = 0
    if session['loginid'] > 0:
        flash('Logged in')
    if session['registered'] > 0:
        flash('Registered')    
    return render_template('index.html')

# This route responds to the registration request
@app.route('/register', methods=['GET','POST'])
def register():
    print ("In register")
    email = "'" + request.form['email'] + "'"
    print (email)
    session['registered'] = 1
    return redirect('/')
    
app.run(debug=True)
