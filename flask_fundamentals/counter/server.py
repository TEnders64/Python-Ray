# Counter
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Godzilla'
@app.route('/', methods=['GET'])
def inc_counter():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template("default.html", count=session['count'])
app.run(debug=True)
