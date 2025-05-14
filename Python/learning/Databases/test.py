import sqlite3

# 1. Connect to (or create) a database
conn = sqlite3.connect('example.db')

# 2. Create a cursor object to execute SQL commands
cur = conn.cursor()

# 3. Create a table
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
''')

# 4. Insert data into the table
cur.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", ("Alice", 30, "alice@example.com"))
cur.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", ("Bob", 25, "bob@example.com"))

# 5. Commit the changes
conn.commit()

# 6. Query data from the table
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
print("All users:")
for row in rows:
    print(row)

# 7. Update data
cur.execute("UPDATE users SET age = ? WHERE name = ?", (31, "Alice"))
conn.commit()

# 8. Delete data
cur.execute("DELETE FROM users WHERE name = ?", ("Bob",))
conn.commit()

# 9. Query again to see changes
cur.execute("SELECT * FROM users")
print("After update and delete:")
for row in cur.fetchall():
    print(row)

# 10. Drop the table (if needed)
# cur.execute("DROP TABLE users")
# conn.commit()

# 11. Close the connection
conn.close()