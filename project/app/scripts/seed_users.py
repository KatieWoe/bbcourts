import psycopg2

# Define your database URL
DATABASE_URL = "postgresql://jjjohnywaffles_k8io_user:vaeBbrGmOq2g6GVR7zttI2g2bsf7Gh8f@dpg-ct1nsddumphs738rb1f0-a.oregon-postgres.render.com/jjjohnywaffles_k8io"

def seed_users():
    """Seeds dummy users into the `users` table."""
    try:
        # Connect to the database
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        # Number of users to seed
        user_count = 5

        # Insert dummy users
        for i in range(1, user_count + 1):
            cursor.execute('''
                INSERT INTO users (userid, name, password)
                VALUES (%s, %s, %s)
                ON CONFLICT (userid) DO NOTHING
            ''', (i, f"User{i}", "password123"))

        # Commit changes
        connection.commit()

        print(f"Successfully seeded {user_count} users into the `users` table.")
    except psycopg2.Error as e:
        print(f"Database error while seeding users: {e}")
    finally:
        # Close the connection
        if connection:
            connection.close()

if __name__ == "__main__":
    seed_users()
