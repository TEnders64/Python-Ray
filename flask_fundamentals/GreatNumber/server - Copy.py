# Great Number Game
from flask import Flask, render_template, request, redirect, session, flash
import random
app = Flask(__name__)
app.secret_key = 'Godzilla'
@app.route('/', methods=['GET','POST'])
def default():
    session['hint'] = 'na'
    if 'num' in session:
        print("Num has value ", session['num'])
        if 'guess' in session:
            print("At root Guess is ",session['guess'])
            if session['guess'].isnumeric():
                guess = int(session['guess'])
                num = int(session['num'])
                if guess == num:
                    session['hint'] = 'equal'
                elif guess > num:
                    session['hint'] = 'high'
                elif guess < num:
                    session['hint'] = 'low'
                print(session['hint'])
                if session['hint'] == 'equal':
                    flash("Success! Your guess of " + session['guess'] + " was correct")
                if session['hint'] == 'high':
                    flash("Sorry. Your guess of " + session['guess'] + " was high")
                if session['hint'] == 'high':
                    flash("Sorry. Your guess of " + session['guess'] + " was low")
                return redirect('/')                    
    else:
        random.seed(None)
        rnum = random.randrange(0, 101)
        session['num'] = rnum
        print ("Random Number: ", session['num'])
    return render_template("default.html", hint=session['hint'])

@app.route('/guess', methods=['POST'])
def guess ():
    session['guess'] = request.form['guess']
    print ("Guess:", session['guess'])
    return redirect('/')
# Game must start here
@app.route('/restart', methods=['GET','POST'])
def restart():
    session.pop('num', None)
    session.pop('guess', None)
    session.pop('hint', None)
    return redirect('/')
app.run(debug=True)
