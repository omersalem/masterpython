# --------------------------------
# -- Flask => Create HTML Files --
# --------------------------------

from flask import Flask, render_template # Import Flask and render_template
# render_template is used to render HTML files
# in the templates folder

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
  return render_template("homepage.html", pagetitle="Homepage") # Render the
  # homepage.html file with a variable pagetitle that can be used in the HTML file
# by using {{ pagetitle }} in the HTML file and we can use multiple variables beside pagetitle
# to render html file we need to create a folder called templates and
# then put the html file in it and the template folder should be in the same
# folder as the python file so here we will create a folder called templates
# and put the homepage.html file in it
@skills_app.route("/about")
def about():
  return render_template("about.html", pagetitle="About Us")
@skills_app.route("/contact")
def contact():
  return render_template("contact.html", pagetitle="Contact Us")
if __name__ == "__main__":
  skills_app.run(debug=True, port=9000)