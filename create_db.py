import psycopg2
from psycopg2 import sql

def create_tables(connection):
    commands = [
        """
        CREATE TABLE courts (
            courtID SERIAL PRIMARY KEY,
            courtName VARCHAR NOT NULL,
            avStar FLOAT DEFAULT NULL,
            nets INTEGER CHECK (nets IN (0, 1)),
            level INTEGER CHECK (level IN (0, 1)),
            clean INTEGER CHECK (clean IN (0, 1)),
            ada INTEGER CHECK (ada IN (0, 1)),
            inOut INTEGER CHECK (inOut IN (0, 1)),
            hours VARCHAR NOT NULL,
            price VARCHAR NOT NULL,
            location VARCHAR NOT NULL
        )
        """,
        """
        CREATE TABLE users (
            userID SERIAL PRIMARY KEY,
            name VARCHAR UNIQUE NOT NULL,
            password VARCHAR NOT NULL
        )
        """,
        """
        CREATE TABLE reviews (
            reviewID SERIAL PRIMARY KEY,
            userID INTEGER NOT NULL REFERENCES users(userID),
            courtID INTEGER NOT NULL REFERENCES courts(courtID),
            star FLOAT CHECK (star BETWEEN 0 AND 5),
            comment VARCHAR DEFAULT ''
        )
        """,
        """
        CREATE TABLE favorites (
            userID INTEGER NOT NULL REFERENCES users(userID),
            courtID INTEGER NOT NULL REFERENCES courts(courtID),
            review FLOAT DEFAULT NULL,
            PRIMARY KEY (userID, courtID)
        )
        """,
        """
        CREATE TABLE photos (
            photoID SERIAL PRIMARY KEY,
            courtID INTEGER NOT NULL REFERENCES courts(courtID),
            photo VARCHAR NOT NULL
        )
        """
    ]
    
    with connection.cursor() as cursor:
        for command in commands:
            cursor.execute(command)
        connection.commit()
        print("Tables created successfully!")

# REQUIRES URL AT THIS POINT
        
if __name__ == "__main__":
    DATABASE_URL = "URL REQUIRED"
    
    try:
        # Connect to the PostgreSQL server
        connection = psycopg2.connect(DATABASE_URL)
        print("Connected to the database successfully!")
        
        # Create tables
        create_tables(connection)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()