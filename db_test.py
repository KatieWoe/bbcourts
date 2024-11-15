# NOTE: This will add these made up values into the db. 
# Run each of the functions independently (comment out all of the functions besides the one you're testing).
# I put them in order of execution. 
# I recommend testing in this order: insert -> select -> remove -> select -> delete
# Remember to delete since this is only test data and we don't actually want this in our database.


import psycopg2
from psycopg2 import sql

def insert_test_data(connection):
    """
    Insert test data into the database.
    """
    with connection.cursor() as cursor:
        # Insert data into the `courts` table
        cursor.execute("""
            INSERT INTO courts (courtName, avStar, nets, level, clean, ada, inOut, hours, price, location)
            VALUES
            ('Court A', 4.5, 1, 1, 1, 1, 0, '9 AM - 9 PM', 'Free', '123 Main St'),
            ('Court B', NULL, 0, 0, 0, 1, 1, '10 AM - 6 PM', '$5', '456 Elm St');
        """)

        # Insert data into the `users` table
        cursor.execute("""
            INSERT INTO users (name, password)
            VALUES
            ('JohnDoe', 'hashed_password_123'),
            ('JaneSmith', 'hashed_password_456');
        """)

        # Insert data into the `reviews` table
        cursor.execute("""
            INSERT INTO reviews (userID, courtID, star, comment)
            VALUES
            (1, 1, 5, 'Great court with excellent amenities!'),
            (2, 2, 3, 'Average court, needs better maintenance.');
        """)

        # Insert data into the `favorites` table
        cursor.execute("""
            INSERT INTO favorites (userID, courtID, review)
            VALUES
            (1, 1, 5),
            (2, 2, 3);
        """)

        # Insert data into the `photos` table
        cursor.execute("""
            INSERT INTO photos (courtID, photo)
            VALUES
            (1, 'link_to_photo_1.jpg'),
            (2, 'link_to_photo_2.jpg');
        """)

        connection.commit()
        print("Test data inserted successfully.")

def select_data(connection):
    """
    Select and display all data from each table.
    """
    tables = ["courts", "users", "reviews", "favorites", "photos"]
    with connection.cursor() as cursor:
        for table in tables:
            print(f"\nData in table '{table}':")
            cursor.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier(table)))
            rows = cursor.fetchall()
            for row in rows:
                print(row)

def remove_data(connection):
    """
    Remove a specific entry from the database.
    """
    with connection.cursor() as cursor:
        # Example: Delete a review
        cursor.execute("DELETE FROM reviews WHERE reviewID = 1;")
        connection.commit()
        print("Deleted review with reviewID = 1.")

def delete_all_data(connection):
    """
    Delete all data from all tables.
    """
    tables = ["reviews", "favorites", "photos", "courts", "users"]
    with connection.cursor() as cursor:
        for table in tables:
            cursor.execute(sql.SQL("DELETE FROM {}").format(sql.Identifier(table)))
        connection.commit()
        print("All data deleted successfully.")

# REQUIRES URL :D
        
if __name__ == "__main__":
    DATABASE_URL = "REQUIRES URL"

    try:
        # Connect to the PostgreSQL server
        connection = psycopg2.connect(DATABASE_URL)
        print("Connected to the database successfully!")

        # Insert test data
        insert_test_data(connection)

        # Select and display data
        select_data(connection)

        # Remove specific data and reselect
        remove_data(connection)
        print("\nData after removal:")
        select_data(connection)

        # Delete all data
        delete_all_data(connection)

        # Verify deletion
        print("\nData after deleting all:")
        select_data(connection)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()