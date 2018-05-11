# DisappearingNinjas
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# The default route will handle rendering our form
@app.route('/')
def index():
  return render_template("default.html")
# notice how we defined which HTTP methods are allowed by this route
@app.route('/ninja', methods=['GET','POST'])
def ShowOneNinja():
  print ("Showing Ninjas")
  color = request.form['color']
  print (color)
  # Does this work?  Yes, but Wrong thing to do
  return render_template('ninja.html', color = color)
app.run(debug=True) # run our server
