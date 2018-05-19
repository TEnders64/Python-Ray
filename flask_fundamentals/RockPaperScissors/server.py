# Rock, Paper, Scissors
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Godzilla'
@app.route('/', methods=['GET', 'POST'])
def show_choices():
    return render_template("default.html")
# Handle form submission
@app.route('/process_play', methods=['POST'])
def play():
    session['choice'] = request.form['choice']  # Post data is here
    print("Player's choice: ", session['choice']) 
    return redirect('/show')
@app.route('/show')
def show():
    return render_template('show.html', choice = session['choice'])
app.run(debug=True)
