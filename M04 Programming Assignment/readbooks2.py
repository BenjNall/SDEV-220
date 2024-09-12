import csv
import sqlite3

# Connect to the SQLite database (books.db)
conn = sqlite3.connect('books.db')
cur = conn.cursor()

# Read the data from books2.csv
with open('C:/Users/fluff/OneDrive/Documents/GitHub/SDEV-220/M04 Programming Assignment/books2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # Skip the header row
    next(reader)
    
    # Insert each row of data into the books table
    for row in reader:
        title, author, year = row
        cur.execute('''
        INSERT INTO books (title, author, year) 
        VALUES (?, ?, ?)
        ''', (title, author, int(year)))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data from books2.csv inserted into books table successfully.")