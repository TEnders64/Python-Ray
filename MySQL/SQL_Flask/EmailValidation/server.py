# Email Validation with DB
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'Godzilla'
mysql = MySQLConnector(app,'mydb')

# index
@app.route('/', methods=['GET'])
def index():
    if 'count' not in session:
        session['count'] = -1
    count = session['count']
    if count == 0:
        flash('Email is NOT valid')
    print('Count = ', session['count'])
    return render_template('index.html', count = count)

# This route responds to the form
@app.route('/process', methods=['POST'])
def validateEmail():
    # Validate email
    email = "'" + request.form['email'] + "'"
    print (email)
    query = "SELECT COUNT(*) FROM emails WHERE email = " + email  # Get number of matches - should be 1
    retVal = mysql.query_db(query)                           # run query with query_db()
    session['count'] = retVal[0]['COUNT(*)']    # SQL output is always a dictionary
    count = int(session['count'])
    if count >= 1:
        flash('Email is valid')
        return render_template('success.html', email = email)
#    elif count == 0:
#        flash('Email is NOT valid')
    return redirect('/')

app.run(debug=True)
