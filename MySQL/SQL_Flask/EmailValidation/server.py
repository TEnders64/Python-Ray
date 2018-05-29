# Email Validation
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'Godzilla'
mysql = MySQLConnector(app,'mydb')

# Below are the friends routes
@app.route('/', methods=['GET'])
def index():
    if 'count' not in session:
        session['count'] = -1    <<<<<<<<<<
    return render_template('index.html'
# This route responds to the form
@app.route('/process', methods=['POST'])
def create():
    # Validate email
    query = "SELECT COUNT(*) FROM emails WHERE email = :email"  # Get number of matches - should be 1
    count = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our template
    return redirect('/')

# Retrieve a record based on url parameter
@app.route('/friends/<friend_id>')
def show(friend_id):
    print("In show")
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id}
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    print(friends)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', one_friend=friends[0])

# Update a record
@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'],
             'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/')

# Delete a record
@app.route('/delete_friend/<friend_id>', methods=['GET'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
