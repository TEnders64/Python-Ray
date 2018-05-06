# Multiple routes
from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)

# Root route
@app.route('/') 
def default():
  return render_template('root.html')   # Return the string as a response.

@app.route('/about')
def about():
  return render_template('about.html')   # Return the string as a response.

@app.route('/projects')
def projects():
  return render_template('projects.html')   # Return the string as a response.

app.run(debug=True)      # Run the app in debug mode.
