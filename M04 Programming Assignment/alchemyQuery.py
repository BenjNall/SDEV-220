from sqlalchemy import create_engine, MetaData, Table, select

# Create a connection to the SQLite database
engine = create_engine('sqlite:///books.db')

# Create a metadata object to hold the information about the tables
metadata = MetaData()

# Reflect the existing books table from the database
books = Table('books', metadata, autoload_with=engine)

# Create a query to select the title column and order it alphabetically
query = select(books.c.title).order_by(books.c.title.asc())

# Execute the query and fetch the results
with engine.connect() as connection:
    result = connection.execute(query)
    
    # Print the titles in alphabetical order
    for row in result:
        print(row.title)

# Output:
# [Running] python -u "c:\Users\fluff\OneDrive\Documents\GitHub\SDEV-220\M04 Programming Assignment\alchemyQuery.py"
# Perdido Street Station
# Small Gods
# The Spellman Files
# The Weirdstone of Brisingamen
# Thud!