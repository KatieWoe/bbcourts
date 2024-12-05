import random
import psycopg2

# Define your database URL
DATABASE_URL = "postgresql://jjjohnywaffles_k8io_user:vaeBbrGmOq2g6GVR7zttI2g2bsf7Gh8f@dpg-ct1nsddumphs738rb1f0-a.oregon-postgres.render.com/jjjohnywaffles_k8io"


def seed_dummy_reviews():
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        # Fetch all court IDs
        cursor.execute("SELECT courtid FROM courts;")
        court_ids = [row[0] for row in cursor.fetchall()]

        for court_id in court_ids:
            # Generate a random number of reviews for each court
            review_count = random.randint(1, 10)
            for _ in range(review_count):
                cursor.execute('''
                    INSERT INTO reviews (userid, courtid, star, comment)
                    VALUES (%s, %s, %s, %s);
                ''', (
                    random.randint(1, 5),  # Random user ID
                    court_id,             # Court ID
                    random.randint(1, 5), # Random star rating
                    "This is a sample review."  # Placeholder comment
                ))

        connection.commit()
        print("Dummy reviews seeded successfully.")

    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    seed_dummy_reviews()
