# --------------------------------------------------------
# -- Databases => SQLite => Create Database And Connect --
# --------------------------------------------------------
# - Connect
# - Execute
# - Close
# --------------------------------------------------

# Import SQLite Module
import sqlite3 # Import SQLite Module so we can use it to create a database and connect to it

# Create Database And Connect
db = sqlite3.connect("app.db") # Create a database file called app.db in the working directory and connect to it

# Create The Tables and Fields
db.execute("create table if not exists skills (name text, progress integer, user_id integer)")
# Create a table called skills with the fields name, progress, and user_id
# we wrote if not exists to avoid error if the table already exists so it won't create it again

# Close Database 
db.close() # Close the database connection


# then we open DBbrowser for sqlite app and open the app.db file to see the table we created