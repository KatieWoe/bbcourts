import psycopg2
from tabulate import tabulate

# Replace with your actual DATABASE_URL
DATABASE_URL = "postgresql://jjjohnywaffles_k8io_user:vaeBbrGmOq2g6GVR7zttI2g2bsf7Gh8f@dpg-ct1nsddumphs738rb1f0-a.oregon-postgres.render.com/jjjohnywaffles_k8io"

def inspect_users():
    """
    Connects to the database and fetches all user information from the 'users' table.
    Prints the data in a tabular format for easy inspection.
    """
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        # Fetch user data
        cursor.execute("SELECT userid, name FROM users;")
        user_data = cursor.fetchall()

        # Display the data in a readable format
        if user_data:
            print("User Data:\n")
            print(tabulate(user_data, headers=["User ID", "Username"], tablefmt="grid"))
        else:
            print("No user data found in the database.")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    inspect_users()
