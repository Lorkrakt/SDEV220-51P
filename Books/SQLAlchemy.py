import sqlalchemy as sa
import pandas as pd

# Create an SQLite engine
engine = sa.create_engine('sqlite:///books.db', echo=True)  # Replace 'books.db' with your desired database name

# Create a metadata object
metadata = sa.MetaData()

# Define the 'books' table
books_table = sa.Table(
    'books',
    metadata,
    sa.Column('title', sa.String(20), primary_key=True),
    sa.Column('author', sa.String(20)),
    sa.Column('year', sa.Integer)
)

# Create the table in the database
metadata.create_all(engine)

#creating the data frame with Panda
csv_file_path = 'books2.csv' #csv file with books in it
df = pd.read_csv(csv_file_path)

#inserting data into books
with engine.connect() as connection:
    df.to_sql('books', con=connection, if_exists='replace', index=False) #establishes connection, replaces if it exists, assumes structure matches

