# ------------------------------------------------------
# -- Databases => SQLite => Insert Data Into Database --
# ------------------------------------------------------
# - cursor => All Operation in SQL Done By Cursor Not The Connection Itself
# - commit => Save All Changes
# ------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db") # Create a database file called app.db in the working directory and connect to it

# Setting Up The Cursor
cr = db.cursor() # Create A Cursor Object To Execute SQL Commands

# Create The Tables and Fields
cr.execute("create table if not exists users (user_id integer, name text)") 
# Create a table called users with the fields user_id and name
cr.execute(
    "create table if not exists skills (name text, progress integer, user_id integer)")

# Inserting Data
# cr.execute("insert into users(user_id, name) values(1, 'Ahmed')")
# cr.execute("insert into users(user_id, name) values(2, 'Sayed')")
# cr.execute("insert into users(user_id, name) values(3, 'Osama')") #this is slow and not recommended the solution
# is by creating a list and looping through it

my_list = ["Ahmed", "Sayed", "Mahmoud", "Ali", "Kamel", "Ibrahim", "Enas"]

for key, user in enumerate(my_list):

     cr.execute(f"insert into users(user_id, name) values({key + 1}, '{user}')") # key + 1 to start from 1 not 0
# we put {user} in single quotes because it's a string and {key + 1} without quotes because it's an integer
# Save (Commit) Changes
db.commit() # Save all changes to the database

# Close Database 
db.close() # Close the database connection