import psycopg2
from psycopg2 import OperationalError, DatabaseError

# Database URL
DATABASE_URL = "postgresql://jjjohnywaffles_k8io_user:vaeBbrGmOq2g6GVR7zttI2g2bsf7Gh8f@dpg-ct1nsddumphs738rb1f0-a.oregon-postgres.render.com/jjjohnywaffles_k8io"


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
    delete_tables()