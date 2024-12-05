import psycopg2
import os

# Define your database URL
DATABASE_URL = "postgresql://jjjohnywaffles_k8io_user:vaeBbrGmOq2g6GVR7zttI2g2bsf7Gh8f@dpg-ct1nsddumphs738rb1f0-a.oregon-postgres.render.com/jjjohnywaffles_k8io"


def inspect_data():
    try:
        # Connect to the database
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        # Query to inspect the `courts` table
        print("Fetching data from the 'courts' table:")
        cursor.execute("SELECT * FROM courts;")
        courts = cursor.fetchall()
        for court in courts:
            print(court)
        
        print("\nCalculating average star ratings and verifying stored `avstar`:")
        # Query to calculate and compare `avstar` dynamically
        cursor.execute('''
            SELECT 
                courts.courtid,
                courts.courtname,
                COALESCE(AVG(reviews.star), 0) AS calculated_avstar,
                courts.avstar AS stored_avstar,
                COUNT(reviews.reviewid) AS total_reviews
            FROM courts
            LEFT JOIN reviews ON courts.courtid = reviews.courtid
            GROUP BY courts.courtid, courts.courtname, courts.avstar
            ORDER BY courts.courtid;
        ''')
        results = cursor.fetchall()
        for row in results:
            print(f"Court ID: {row[0]}, Name: {row[1]}, Calculated Avg Star: {row[2]}, Stored Avg Star: {row[3]}, Total Reviews: {row[4]}")
        
        print("\nFetching photos linked to courts:")
        # Query to inspect the `photos` table
        cursor.execute('''
            SELECT courts.courtid, courts.courtname, photos.photo
            FROM courts
            LEFT JOIN photos ON courts.courtid = photos.courtid
            ORDER BY courts.courtid;
        ''')
        photos = cursor.fetchall()
        for photo in photos:
            print(photo)

    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    inspect_data()
