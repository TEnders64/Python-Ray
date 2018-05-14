# DisappearingNinjas
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# The default route will handle rendering our form
@app.route('/')
def index():
  return render_template("default.html")
# notice how we defined which HTTP methods are allowed by this route
@app.route('/ninja', methods=['GET','POST'])
def ShowAllNinja():
  print ("Showing Ninjas")
  # Does this work?  Yes, but Wrong thing to do
  return render_template('showNinjas.html')
@app.route('/ninja/<color>', methods=['GET','POST'])
def ShowOneNinja(color):
  color=color
  print('Color from URL: ', color)
  return render_template('ninja.html', color = color)
app.run(debug=True) # run our server
