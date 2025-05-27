# ------------------------------------
# -- Flask => Jinja Template Engine --
# ------------------------------------
# # Jinja is a template engine for Python that allows you to create dynamic HTML pages.
# It is used in Flask to render HTML templates with variables and control structures.

# we will install jinja on vscode so we can use it in our flask app
# ------------------------------------
# the main app file will be the same as the previous one but we change in html files
# and here we will use pages homes and abouts instead of home and about html files
# and we will create a bases.html file instead of base.html file to extend it
# and we will create two css files inside the css folder which is inside the static folder
# ------------------------------------
# we will use <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}" /> 
# in the bases.html file to link the css file and this is jinja syntax to link the css file   
# ------------------------------------
from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
  return render_template("homes.html", title="Homepage")

@skills_app.route("/about")
def about():
  return render_template("abouts.html", title="About Us")

if __name__ == "__main__":
  skills_app.run(debug=True, port=9000)