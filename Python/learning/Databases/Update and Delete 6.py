# ----------------------------------------------
# -- Databases => SQLite => Update and Delete --
# ----------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db") # Create a database file called app.db in the working directory and connect to it

# Setting Up The Cursor
cr = db.cursor() # Create A Cursor Object To Execute SQL Commands
cr.execute("create table if not exists users (user_id integer, name text)") # Create a table called users
cr.execute("insert into users(user_id, name) values(1, 'Ahmed')") #inserting data into the users table
cr.execute("insert into users(user_id, name) values(2, 'Sayed')")
cr.execute("insert into users(user_id, name) values(3, 'Osama')")
cr.execute("insert into users(user_id, name) values(4, 'Ali')")
#with the fields user_id and name




# ⁡⁢⁣⁣Update Data so we can edit the data in the table⁡
cr.execute("update users set name = 'Mahmoud' where user_id = 1")
cr.execute("update users set name = 'Ameer' where user_id = 2") 
cr.execute("update users set name = 'Sayed' where user_id = 3")
cr.execute("update users set name = 'khalil' where user_id = 4")




# ⁡⁢⁣⁣Delete Data⁡
#cr.execute("delete from users where user_id = 1") # delete the row where user_id = 1

# ⁡⁢⁣⁣Fetch Data⁡
cr.execute("select * from users")

print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

# ⁡⁢⁣⁣Save (Commit) Changes⁡
db.commit()

# ⁡⁢⁣⁣Close Database⁡
db.close()