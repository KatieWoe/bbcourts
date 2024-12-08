import random
import psycopg2

# Define your database URL
DATABASE_URL = "postgresql://jjjohnywaffles_k8io_user:vaeBbrGmOq2g6GVR7zttI2g2bsf7Gh8f@dpg-ct1nsddumphs738rb1f0-a.oregon-postgres.render.com/jjjohnywaffles_k8io"

def delete_all_reviews():
    """Deletes all existing reviews from the database."""
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        
        cursor.execute('DELETE FROM reviews')
        connection.commit()
        print("Successfully deleted all existing reviews.")
        
    except psycopg2.Error as e:
        print(f"Database error while deleting reviews: {e}")
    finally:
        if connection:
            connection.close()

def seed_dummy_reviews():
    """Seeds new reviews with random ratings and comments."""
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        # Fetch all court IDs
        cursor.execute("SELECT courtid FROM courts;")
        court_ids = [row[0] for row in cursor.fetchall()]

        sample_comments = [
            "Great court, well maintained!",
            "Decent spot for pickup games.",
            "Needs better lighting at night.",
            "Perfect for practice sessions.",
            "Love the location, but crowded on weekends.",
            "Rims need maintenance.",
            "Excellent surface, no cracks.",
            "Good court, friendly community.",
            "Could use better backboards.",
            "Nice place to shoot around."
        ]

        for court_id in court_ids:
            # Generate a random number of reviews for each court
            review_count = random.randint(3, 15)  # Increased range for more variety
            for _ in range(review_count):
                cursor.execute('''
                    INSERT INTO reviews (userid, courtid, star, comment)
                    VALUES (%s, %s, %s, %s);
                ''', (
                    random.randint(1, 25),  # Random user ID from new user set
                    court_id,               # Court ID
                    random.randint(1, 5),   # Random star rating
                    random.choice(sample_comments)  # Random comment from our list
                ))

        connection.commit()
        print("New reviews seeded successfully.")

    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    delete_all_reviews()    # First delete all existing reviews
    seed_dummy_reviews()    # Then seed new reviews