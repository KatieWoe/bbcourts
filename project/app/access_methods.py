import psycopg2
import random

DATABASE_URL = "postgresql://jjjohnywaffles_k8io_user:vaeBbrGmOq2g6GVR7zttI2g2bsf7Gh8f@dpg-ct1nsddumphs738rb1f0-a.oregon-postgres.render.com/jjjohnywaffles_k8io"

def createCourt(cursor, courtName, nets, level, clean, ada, inOut, hours, price, location):
    """
    Inserts a new court into the database and returns its ID.
    """
    cursor.execute('''
        INSERT INTO courts (courtName, avStar, nets, level, clean, ada, inOut, hours, price, location)
        VALUES (%s, NULL, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING courtID;
    ''', (courtName, nets, level, clean, ada, inOut, hours, price, location))
    court_id = cursor.fetchone()[0]
    return court_id

'''
def createCourt(courtName, nets, level, clean, ada, inOut, hours, price, location):
    connection = psycopg2.connect(DATABASE_URL)
    try:
        with connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO courts (courtName, avStar, nets, level, clean, ada, inOut, hours, price, location)
                VALUES (%s, NULL, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING courtID;
            ''', (courtName, nets, level, clean, ada, inOut, hours, price, location))
            court_id = cursor.fetchone()[0]
        connection.commit()
        return court_id
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
'''
            
def getCourt(cursor, courtID_get):
    """
    Retrieve all details of a court by its ID. Returns a tuple with all court elements.
    """
    cursor.execute('''
        SELECT * FROM courts WHERE courtID = %s;
    ''', (courtID_get,))
    court = cursor.fetchone()  # Fetch one row directly
    return court

def deleteCourt(cursor, courtID_del):
    """
    Deletes the court with the specified ID from the database.
    """
    cursor.execute('''
        DELETE FROM courts WHERE courtID = %s;
    ''', (courtID_del,))



def calcAvStar(connection, courtID_calc):
    """
    Get the star rating from reviews for the court given. Calculate the average and return the average.
    """
    connection = psycopg2.connect("postgresql://jjjohnywaffles_k8io_user:vaeBbrGmOq2g6GVR7zttI2g2bsf7Gh8f@dpg-ct1nsddumphs738rb1f0-a.oregon-postgres.render.com/jjjohnywaffles_k8io")
    cur = connection.cursor()
    cur.execute('''
    SELECT star FROM reviews WHERE courtID=?;
    ''', (courtID_calc))
    
    stars_tup = cur.fetchall()
    stars = []
    for row in stars_tup:
        stars.append(row[0])
    avStar = sum(stars) / len(stars)
    #May want to also edit courts entry to include this new value
    connection.commit()
    connection.close()
    return avStar

def editCourt(connection, courtID_edit, courtName, avStar, nets, level, clean, ada, inOut, hours, price, location):
    """
    Edit the court with the ID given so that all the parameters are now used.
    """
    connection = psycopg2.connect(DATABSE_URL)
    cur = connection.cursor()
    cur.execute('''
    UPDATE courts SET courtName=?, avStar=?, nets=?, level=?, clean=?, ada=?, inOut=?, hours=?, price=?, location=? WHERE courtID=?;
    ''', (courtName, avStar, nets, level, clean, ada, inOut, hours, price, location, courtID_edit))
    connection.commit()
    connection.close()
    return

def findCourts(connection, search_term):
    """
    Search the courts table in both the name and location atributes and return a list of IDs that pulled up matches.
    """
    connection = psycopg2.connect(DATABSE_URL)
    cur = connection.cursor()
    cur.execute('''
    SELECT courtID FROM courts WHERE courtName LIKE ?;
    ''', (search_term))
    names_tup = cur.fetchall()
    names = []
    for row in names_tup:
        names.append(row[0])
    cur.execute('''
    SELECT courtID FROM courts WHERE location LIKE ?;
    ''', (search_term))
    loc_tup = cur.fetchall()
    locs = []
    for row in loc_tup:
        locs.append(row[0])
    bothlists = list(set(names) | set(locs))
    connection.commit()
    connection.close()
    return bothlists

def createReview(connection, userID, courtID, comment, star):
    """
    Create a review with a comment and a star review. Creates a random unique id. Returns that id.
    """
    connection = psycopg2.connect(DATABSE_URL)
    cur = connection.cursor()
    
    """
    cur.execute('''
    SELECT reviewID FROM reviews;
    ''')
    ids_tup = cur.fetchall()
    ids = []
    for row in ids_tup:
        ids.append(row[0])
    maybe_id = random.randint(10000, 99999)
    while maybe_id in ids:
        maybe_id = random.randint(10000, 99999)
    """
    
    cur.execute('''
    INSERT INTO reviews VALUES (?, ?, ?, ?) RETURNING reviewID;
    ''',(userID, courtID, star, comment))
    id_of_new_row = cur.fetchone()[0]
    
    connection.commit()
    connection.close()
    return id_of_new_row

def getReviews(connection, courtID):
    """
    Get the reviews or a given court. Returns a dictionary with the key being the review ids, and the values a list of the other elements.
    """
    connection = psycopg2.connect(DATABSE_URL)
    cur = connection.cursor()
    cur.execute('''
    SELECT * FROM reviews WHERE courtID=?;
    ''', (courtID))
    rev_tup = cur.fetchall()
    reviews = {}
    for row in rev_tup:
        reviews[row[0]] = [row[1], row[2], row[3], row[4]]
    connection.commit()
    connection.close()
    return reviews

def getUserReviews(connection, userID):
    """
    Get the reviews made by a given user. Return a dictionary with the key being the review ids, and the values a list of the other elements.
    """
    connection = psycopg2.connect(DATABSE_URL)
    cur = connection.cursor()
    cur.execute('''
    SELECT * FROM reviews WHERE userID=?;
    ''', (userID))
    rev_tup = cur.fetchall()
    reviews = {}
    for row in rev_tup:
        reviews[row[0]] = [row[1], row[2], row[3], row[4]]
    connection.commit()
    connection.close()
    return reviews


if __name__ == "__main__":
    """
    Main function to test functions.
    """
    # Define the database URL
    DATABASE_URL = "postgresql://jjjohnywaffles_k8io_user:vaeBbrGmOq2g6GVR7zttI2g2bsf7Gh8f@dpg-ct1nsddumphs738rb1f0-a.oregon-postgres.render.com/jjjohnywaffles_k8io"
    try:
        # Connect to the database
        connection = psycopg2.connect(DATABASE_URL)
        with connection.cursor() as cursor:
            
            # TESTING CREATE COURT
            # Define test data for creating a court
            test_court = {
                "courtName": "Test Court",
                "nets": 1,
                "level": 1,
                "clean": 1,
                "ada": 1,
                "inOut": 0,
                "hours": "9 AM - 9 PM",
                "price": "Free",
                "location": "123 Test Street",
            }

            # Call the createCourt function
            print("\nTesting createCourt:")
            court_id = createCourt(
                cursor,
                test_court["courtName"],
                test_court["nets"],
                test_court["level"],
                test_court["clean"],
                test_court["ada"],
                test_court["inOut"],
                test_court["hours"],
                test_court["price"],
                test_court["location"],
            )
            print(f"Court created with ID: {court_id}")
            
            
            # TESTING GETCOURT
            # Call the getCourt function
            print("\nTesting getCourt:")
            court_details = getCourt(cursor, court_id)
            print(f"Retrieved court: {court_details}")

            # Verify the retrieved court matches the input
            expected_result = (
                court_id,
                test_court["courtName"],
                None,  # avStar defaults to NULL
                test_court["nets"],
                test_court["level"],
                test_court["clean"],
                test_court["ada"],
                test_court["inOut"],
                test_court["hours"],
                test_court["price"],
                test_court["location"],
            )
            assert court_details == expected_result, f"Test failed: {court_details} != {expected_result}"
            print("getCourt test passed successfully.")
            
            '''
            # TESTING DELETE
            # Call the deleteCourt function
            print("\nTesting deleteCourt:")
            deleteCourt(cursor, court_id)
            print(f"Court with ID {court_id} deleted successfully.")

            # Verify the court no longer exists
            cursor.execute("SELECT * FROM courts WHERE courtID = %s;", (court_id,))
            deleted_court = cursor.fetchone()
            assert deleted_court is None, f"Test failed: Court with ID {court_id} still exists."
            print("deleteCourt test passed successfully.")
            '''
            
        connection.commit()

    except Exception as e:
        print(f"Error during test: {e}")
        if 'connection' in locals():
            connection.rollback()  # Rollback transaction on error

    finally:
        # Close the connection
        if 'connection' in locals() and connection:
            connection.close()
            print("Connection closed.")