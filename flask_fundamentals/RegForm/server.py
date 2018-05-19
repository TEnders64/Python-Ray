# Registration Form
from flask import Flask, render_template, request, redirect, session, flash
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'Godzilla'

# our index route will handle rendering our form
@app.route('/')
def default():
   return render_template("index.html")
# this route will handle our form submission
@app.route('/process', methods=['POST'])
def process():
  print ("Got Post Info")
  email = request.form['email'] 
  print (email)
  if len(email) < 1:
     flash("Email required!") # just pass a string to the flash function
     return redirect('/')
  elif not EMAIL_REGEX.match(request.form['email']):
     flash("Invalid Email Address!")   
     return redirect('/')
  else:
     flash("Success! ")    
     return redirect('/')
# Return from info page
@app.route('/restart')
def restart():
  return redirect('/')
app.run(debug=True) # run our server
