from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.copy
@app.route('/Hello')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # http://localhost:5000/Hello we will run the following "hello_world" function.
def HW():
  return render_template('hello.html')   # Return the string as a response.
app.run(debug=True)      # Run the app in debug mode.