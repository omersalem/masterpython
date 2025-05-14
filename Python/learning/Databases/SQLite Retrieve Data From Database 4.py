# --------------------------------------------------------
# -- Databases => SQLite => Retrieve Data From Database --
# --------------------------------------------------------
# - fetchone => returns a single record or None if no more rows are available.
# - fetchall => fetches all the rows of a query result. It returns all the rows
#               as a list of tuples. An empty list is returned if there is no record to fetch.
# - fetchmany(size) =>
# ------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()

# Create The Tables and Fields
cr.execute("create table if not exists users (user_id integer, name text)")
cr.execute("create table if not exists skills (name text, progress integer, user_id integer)")

# Inserting Data
cr.execute("insert into users(user_id, name) values(1, 'Ahmed')") #inserting data into the users table
cr.execute("insert into users(user_id, name) values(2, 'Sayed')")
cr.execute("insert into users(user_id, name) values(3, 'Osama')")

# Fetch Data
cr.execute("select * from skills") #fetching data from the skills table * means all the columns

print(cr.fetchone()) #fetchone returns a single record or None if no more rows are available.
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone()) #this will return None because there is no more data to fetch

print(cr.fetchall()) #fetchall fetches all the rows of a query result. It returns all the rows
# as a list of tuples. An empty list is returned if there is no record to fetch.

print(cr.fetchmany(2)) #fetchmany(size) fetches the next set of rows of a query result, 
#returning a list. An empty list is returned when no more rows are available. 

# Save (Commit) Changes
db.commit()

# Close Database
db.close()