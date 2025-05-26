# ----------------------------------------
# -- Flask => Intro and Your First Page --
# ----------------------------------------
# - Flask Is Micro Framework Built With Python
# --------------------------------------------
# - HTML
# - CSS
# - JavaScript
# --------------------------------------------
# install flask using pip
# pip install flask

from flask import Flask # Import Flask 

skills_app = Flask(__name__)  # Create Flask App Instance called skills_app
# __name__ is a special variable in Python that represents the name
#  of the current module.

@skills_app.route("/") # Define the route for the homepage
def homepage(): # This function will be called when the user visits the homepage
  # The function returns a string that will be displayed on the homepage
  return "Hello From Flask Framework"

@skills_app.route("/about") # Define the route for the about page
def about(): # This function will be called when the user visits the about page
  return "About Page From Flask Framework" 

if __name__ == "__main__": # This block ensures that the app runs only if
  # this script is executed directly
  skills_app.run(debug=True, port=9000) # Run the Flask app with debug mode 
  # enabled and on port 9000

  # to open the web page, open a web browser and go to:
  # http://127.0.0.1:9000
  # to open about page, go to:
  # http://127.0.0.1:9000/about