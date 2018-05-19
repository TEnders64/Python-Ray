# Great Number Game
from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'Godzilla'
@app.route('/', methods=['GET'])
def inc_counter():
    if 'num' in session:
        print("Num has value ", session['num'])
    else:
        random.seed()
        rnum = random.randrange(0, 101)
        session['num'] = rnum
        print("New num ",rnum)
    print ("Random Number: ", session['num'])
    return render_template("default.html", num=session['num'])
# Game must start here
@app.route('/restart', methods=['GET','POST'])
def restart():
    session.pop('num', None)
    return redirect('/')
app.run(debug=True)
