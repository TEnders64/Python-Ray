from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# Landing Page
# our index route will handle rendering our form
@app.route('/dojos/new') #methods=['POST'])
def create_user():
   print ("Got Post Info")
   # redirects back to the '/' route
   print ("Getting Post Info")
   return render_template("dojos.html")
@app.route('/users', methods=['POST'])
def users():
   name = request.form['name']
   email = request.form['email']
   return render_template("users.html")  
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/ninjas')
def ninjas():
   print ("In ninjas")
   return render_template("ninjas.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

app.run(debug=True) # run our server
