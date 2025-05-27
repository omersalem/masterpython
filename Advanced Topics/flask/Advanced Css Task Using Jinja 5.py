# --------------------------------------------
# -- Flask => Advanced Css Task Using Jinja --
# --------------------------------------------
# in this task we will create css file specific for homepage and add page and also 
# we will use the css files of the base.html file and for about page we will use the css file
#  of the base.html only without creating a new css file for it
# and here we will h.html instead of home.html and a.html instead of about.html and
# b.html instead of base.html and we will create a new html file called add.html for the add page
# --------------------------------------------
from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
  return render_template("h.html",
                          title="Homepage",
                          custom_css="home")
@skills_app.route("/add")
def add():
  return render_template("add.html",
                          title="Add Skill",
                          custom_css="add")

@skills_app.route("/about")
def about():
  return render_template("a.html", title="About Us")

if __name__ == "__main__":
  skills_app.run(debug=True, port=9000)