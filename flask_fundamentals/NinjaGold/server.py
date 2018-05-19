# Ninja Gold
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Godzilla'
# our index route will handle rendering our form
@app.route('/')
def default():
   if 'money' not in session:
     session['money'] = 0
   return render_template("default.html", money=session['money'])
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/process_money', methods=['POST'])
def process_money():
   place = request.form['action']
   session['money'] += 1
   print ("Place is ", place, "Money is ", session['money'])
   # redirects back to the '/' route
   return redirect('/')
app.run(debug=True) # run our server
