 # The Wall
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from hashlib import md5
import re
app = Flask(__name__)
app.secret_key = 'Godzilla'
mysql = MySQLConnector(app,'TheWall')

# index
@app.route('/', methods=['GET'])
def index():
    if 'loginid' not in session:
        session['loginid'] = 0
    if 'registered' not in session:
        session['registered'] = 0
    if session['loginid'] > 0:
        flash('Logged in')
        # Doesn't work because session variables are stored in cookies
        #return render_template('messages.html', userID = session['loginid'])
    if session['registered'] > 0:
        flash('Registered')    
    return render_template('index.html')

# This route responds to the registration request
@app.route('/register', methods=['GET','POST'])
def register():
    print ("In register")
    email = request.form['email']
    first_name  = request.form['first_name']
    last_name  = request.form['last_name']
    password = request.form['password']
    # Using Python 3 hashlib
    m = md5()
    pw = md5(password.encode('utf-8')).hexdigest()
    print (password)
    print(pw)
    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
        'first_name': first_name,
        'last_name':  last_name,
        'email': email,
	'password': pw
    }
    print (data)
    # Run query, with dictionary values injected into the query.
    rslt = mysql.query_db(query, data)
    print ('rslt = ', rslt)
    # Get id of just registered user from rslt
    session['loginid'] = int(rslt)
    session['registered'] = 1
    flash('Registration complete.  You are now logged in')
    return render_template('messages.html', userID = session['loginid'])      # <<<<<
    #return redirect('/')

@app.route('/login', methods=['POST'])
def validateLogin():
    email = "'" + request.form['email'] + "'"  # Quotes so we can just concatentate into query string
    password = request.form['password']
    m = md5()
    pw = md5(password.encode('utf-8')).hexdigest()
    print (password)
    print(pw)
    session['loginid'] = 0 # Assume failure
    # >>>>. Get id with matching email and password
    query = "SELECT id FROM users WHERE email = " + email + " AND password = '" + pw + "'"
    retVal = mysql.query_db(query)               # run query with query_db()
    if len(retVal) > 0:
        session['loginid'] = retVal[0]['id']    # SQL output is always a dictionary
        print ("retval = ", retVal, "session['loginid']", session['loginid'])
        if session['loginid'] >= 1:
            flash('Logged in')
            return redirect('/getMessages')
    else:
        flash('Email NOT found')
    return redirect('/')

@app.route('/getMessages', methods=['GET'])
def getMessages():
    query = "Select * FROM messages WHERE user_id = " + session['loginid']
    messages = mysql.query_db(query)
    return render_template('messages.html', messages = messages)

app.run(debug=True)
