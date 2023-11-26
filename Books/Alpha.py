import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create an SQLite engine
engine = sa.create_engine('sqlite:///books.db', echo=True)

# Define the ORM (Object-Relational Mapping) class
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    title = sa.Column(sa.String(50), primary_key=True)
    author = sa.Column(sa.String(50))
    year = sa.Column(sa.Integer)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Query the title column from the 'book' table in alphabetical order
query_result = session.query(Book.title).order_by(Book.title).all()

# Print the results
for title in query_result:
    print(title[0])
