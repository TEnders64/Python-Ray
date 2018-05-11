# Dojo Survey
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['GET','POST'])
def create_user():
  print ("Got Post Info")
  name = request.form['yourname'] 
  location = request.form['location']
  lang = request.form['lang']
  comment = request.form['comment']
  print (name)
   # Does this work?  Yes, but Wrong thing to do
  return render_template('info.html', name = name, location = location, lang = lang, comment = comment)
app.run(debug=True) # run our server
