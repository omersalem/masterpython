# ----------------------------------------------
# -- Flask => Create & Extends Html Templates --
# ----------------------------------------------

from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
  return render_template("home.html", pagetitle="Homepage")

@skills_app.route("/about")
def about():
  return render_template("aboutpage.html", pagetitle="About Us")
@skills_app.route("/contact")
def contact():
  return render_template("contact.html", pagetitle="Contact Us")

if __name__ == "__main__":
  skills_app.run(debug=True, port=9000)

  