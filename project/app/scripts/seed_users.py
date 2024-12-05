import psycopg2
import random

# Define your database URL
DATABASE_URL = "postgresql://jjjohnywaffles_k8io_user:vaeBbrGmOq2g6GVR7zttI2g2bsf7Gh8f@dpg-ct1nsddumphs738rb1f0-a.oregon-postgres.render.com/jjjohnywaffles_k8io"

# List of common first names
first_names = [
    "James", "John", "Robert", "Michael", "William", "David", "Joseph", "Thomas",
    "Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia",
    "Liam", "Noah", "Oliver", "Elijah", "Lucas", "Mason", "Logan", "Alexander",
    "Sarah", "Emily", "Madison", "Elizabeth", "Ella", "Catherine", "Victoria", "Grace"
]

# List of letters for last initials
last_initials = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def delete_all_users():
    """Deletes all users from the users table."""
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        
        cursor.execute('DELETE FROM users')
        connection.commit()
        print("Successfully deleted all users from the database.")
        
    except psycopg2.Error as e:
        print(f"Database error while deleting users: {e}")
    finally:
        if connection:
            connection.close()

def seed_users():
    """Seeds users with first names and last initials into the `users` table."""
    try:
        # Connect to the database
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        # Number of users to seed
        user_count = 25

        # Insert users with random first names and last initials
        for i in range(1, user_count + 1):
            first_name = random.choice(first_names)
            last_initial = random.choice(last_initials)
            name = f"{first_name} {last_initial}."
            
            cursor.execute('''
                INSERT INTO users (userid, name, password)
                VALUES (%s, %s, %s)
                ON CONFLICT (userid) DO NOTHING
            ''', (i, name, "password123"))

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
    delete_all_users()  # First delete all existing users
    seed_users()        # Then seed new users