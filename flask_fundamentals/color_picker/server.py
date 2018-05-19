# Color Picker
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def show_index():
    return render_template("index.html", RGBVal = -1)
# Handle form submission
@app.route('/SetBckgnd', methods=['POST'])
def setBackground():
    rgbval = request.form['RGBVal']
    print("Got color value", rgbval)
    return render_template("index.html", RGBVal = rgbval)
    #return redirect('/', RGBVal = rgbval)
app.run(debug=True)
