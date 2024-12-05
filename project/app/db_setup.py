import psycopg2
from psycopg2 import OperationalError, DatabaseError

# Database URL
#DATABASE_URL = "postgresql://jae_test_user:HtuRJ21AGVyAfz4e2rERt9n8ErU7Wupf@dpg-ct85p923esus73a5lba0-a.frankfurt-postgres.render.com/jae_test"
DATABASE_URL = "postgresql://jjjohnywaffles_k8io_user:vaeBbrGmOq2g6GVR7zttI2g2bsf7Gh8f@dpg-ct1nsddumphs738rb1f0-a.oregon-postgres.render.com/jjjohnywaffles_k8io"

def create_tables():
    commands = [
        """
        CREATE TABLE IF NOT EXISTS courts (
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
            location VARCHAR NOT NULL,
            description TEXT NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS users (
            userID SERIAL PRIMARY KEY,
            name VARCHAR UNIQUE NOT NULL,
            password VARCHAR NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS reviews (
            reviewID SERIAL PRIMARY KEY,
            userID INTEGER NOT NULL REFERENCES users(userID),
            courtID INTEGER NOT NULL REFERENCES courts(courtID),
            star FLOAT CHECK (star BETWEEN 0 AND 5),
            comment VARCHAR DEFAULT ''
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS favorites (
            userID INTEGER NOT NULL REFERENCES users(userID),
            courtID INTEGER NOT NULL REFERENCES courts(courtID),
            review FLOAT DEFAULT NULL,
            PRIMARY KEY (userID, courtID)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS photos (
            photoID SERIAL PRIMARY KEY,
            courtID INTEGER NOT NULL REFERENCES courts(courtID),
            photo VARCHAR NOT NULL
        )
        """
    ]
    conn = None
    try:
        # Connect to the database
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        # Execute each command
        for command in commands:
            cur.execute(command)
        conn.commit()
        print("Tables created successfully!")
    except (OperationalError, DatabaseError) as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def delete_tables():
    commands = [
        "DROP TABLE IF EXISTS photos CASCADE",
        "DROP TABLE IF EXISTS favorites CASCADE",
        "DROP TABLE IF EXISTS reviews CASCADE",
        "DROP TABLE IF EXISTS users CASCADE",
        "DROP TABLE IF EXISTS courts CASCADE"
    ]
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        conn.commit()
        print("Tables deleted successfully!")
    except (OperationalError, DatabaseError) as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_tables()
