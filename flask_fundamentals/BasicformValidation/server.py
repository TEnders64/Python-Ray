# Basic Form Validation
from flask import Flask, render_template, request, redirect, session, flash
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
  name = request.form['yourname'] 
  location = request.form['location']
  lang = request.form['lang']
  comment = request.form['comment']
  print (name)
  if len(name) < 1:
    flash("Name cannot be empty!") # just pass a string to the flash function
    return redirect('/')
  elif len(comment) > 120:
    flash("Comment too long!")
    return redirect('/')
  else:
    flash("Success! Your name is name")    
   # Does this work?  Yes, but Wrong thing to do
  return render_template('info.html', name = name, location = location, lang = lang, comment = comment)
# Return from info page
@app.route('/restart')
def restart():
  return redirect('/')
app.run(debug=True) # run our server
