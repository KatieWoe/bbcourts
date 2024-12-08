import psycopg2

# Replace this with your actual database URL
DATABASE_URL = "postgresql://jjjohnywaffles_k8io_user:vaeBbrGmOq2g6GVR7zttI2g2bsf7Gh8f@dpg-ct1nsddumphs738rb1f0-a.oregon-postgres.render.com/jjjohnywaffles_k8io"

def update_average_star_ratings():
    """
    Updates the avstar column in the courts table with the calculated average star ratings
    based on the reviews table.
    """
    try:
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        
        # Fetch all court IDs from the courts table
        cursor.execute("SELECT courtid FROM courts;")
        court_ids = [row[0] for row in cursor.fetchall()]
        
        for court_id in court_ids:
            # Calculate the average star rating for the current court
            cursor.execute("""
                SELECT AVG(star) FROM reviews WHERE courtid = %s;
            """, (court_id,))
            avg_star = cursor.fetchone()[0]
            avg_star = avg_star or 0.0  # Default to 0 if no reviews
            
            # Update the avstar column for the current court
            cursor.execute("""
                UPDATE courts SET avstar = %s WHERE courtid = %s;
            """, (avg_star, court_id))
        
        connection.commit()
        print("Updated average star ratings successfully.")
    except psycopg2.Error as e:
        print(f"Database error while updating average star ratings: {e}")
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    update_average_star_ratings()
