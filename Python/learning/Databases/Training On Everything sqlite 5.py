# ---------------------------------------------------
# -- Databases => SQLite => Training On Everything --
# ---------------------------------------------------
# it is better to delete the app.db so start from scratch

import sqlite3

def get_all_data(): # Function To Get All Data From Database

  try: 

    # Connect To Database
    db = sqlite3.connect("app.db") # Connect To Database File and create it if not exists

    # Print Success Message
    print("Connected To Database Successfully") 

    # Setting Up The Cursor
    cr = db.cursor() # Create A Cursor Object To Execute SQL Commands
    # Create The Tables and Fields
    cr.execute("create table if not exists users (user_id integer, name text)")
    # insert some data into the users table
    cr.execute("insert into users(user_id, name) values(1, 'Ahmed')")
    cr.execute("insert into users(user_id, name) values(2, 'Sayed')")
    cr.execute("insert into users(user_id, name) values(3, 'Osama')") #this is slow and not recommended the solution



    # Fetch Data From Database
    cr.execute("select * from users") # Fetching All Data From Users Table

    # Assign Data To Variable
    results = cr.fetchall() # store the results in a variable called results

    # Print Number Of Rows
    print(f"Database Has {len(results)} Rows.") # Print Number Of Rows In Database 
    # here the result is a list of tuples so we can use len() to get the number of rows

    # Printing Message
    print("Showing Data:") 

    # Loop On Results
    for row in results: # Loop On Rows so each row is a tuple

      print(f"UserID => {row[0]},", end=" ") # Print UserID which is the first element in the tuple (row[0])

      print(f"Username => {row[1]}") # Print Username which is the second element in the tuple (row[1])

  except sqlite3.Error as er: # Catch Any Error

    print(f"Error Reading Data {er}") # Print Error Message

  finally: # Run This Code No Matter What

    if (db): # Check If Database Is Open

      # Close Database Connection
      db.close()

      print("Connection To Database Is Closed")

get_all_data() # Call The Function To Get All Data From Database