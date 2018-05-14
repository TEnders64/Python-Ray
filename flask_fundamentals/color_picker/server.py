# Color Picker
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def show_index():
    return render_template("index.html")
app.run(debug=True)
