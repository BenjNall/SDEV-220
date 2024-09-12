import sqlite3

# Connect to the SQLite database (books.db)
conn = sqlite3.connect('books.db')
cur = conn.cursor()

# Create the 'books' table if it doesn't exist
cur.execute('''
CREATE TABLE IF NOT EXISTS books (
    title TEXT,
    author TEXT,
    year INTEGER
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Table 'books' created (if it didn't exist).")