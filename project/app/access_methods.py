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

"""
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
"""
            
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



def calcAvStar(cursor, courtID_calc):
    """
    Get the star rating from reviews for the court given. Calculate the average and return the average.
    """
    cursor.execute('''
    SELECT star FROM reviews WHERE courtID = %s;
    ''', (courtID_calc,))
    
    stars_tup = cursor.fetchall()
    stars = []
    for row in stars_tup:
        stars.append(row[0])
    avStar = sum(stars) / len(stars)
    #May want to also edit courts entry to include this new value
    return avStar

def editCourt(cursor, courtID_edit, courtName, avStar, nets, level, clean, ada, inOut, hours, price, location):
    """
    Edit the court with the ID given so that all the parameters are now used.
    """
    cursor.execute('''
    UPDATE courts SET courtName=%s, avStar=%s, nets=%s, level=%s, clean=%s, ada=%s, inOut=%s, hours=%s, price=%s, location=%s WHERE courtID=%s;
    ''', (courtName, avStar, nets, level, clean, ada, inOut, hours, price, location, courtID_edit))
    return

def findCourts(cursor, search_term):
    """
    Search the courts table in both the name and location atributes and return a list of IDs that pulled up matches.
    """
    cursor.execute('''
    SELECT courtID FROM courts WHERE courtName LIKE %s;
    ''', (search_term))
    names_tup = cursor.fetchall()
    names = []
    for row in names_tup:
        names.append(row[0])
    cursor.execute('''
    SELECT courtID FROM courts WHERE location LIKE %s;
    ''', (search_term))
    loc_tup = cur.fetchall()
    locs = []
    for row in loc_tup:
        locs.append(row[0])
    bothlists = list(set(names) | set(locs))
    return bothlists

def createReview(cursor, userID, courtID, comment, star):
    """
    Create a review with a comment and a star review. Creates a random unique id. Returns that id.
    """
    
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
    
    cursor.execute('''
    INSERT INTO reviews (userID, courtID, star, comment) VALUES (%s, %s, %s, %s) RETURNING reviewID;
    ''',(userID, courtID, star, comment))
    id_of_new_row = cur.fetchone()[0]
    
    return id_of_new_row

def getReviews(cursor, courtID):
    """
    Get the reviews or a given court. Returns a dictionary with the key being the review ids, and the values a list of the other elements.
    """
    cursor.execute('''
    SELECT * FROM reviews WHERE courtID = %s;
    ''', (courtID))
    rev_tup = cur.fetchall()
    reviews = {}
    for row in rev_tup:
        reviews[row[0]] = [row[1], row[2], row[3], row[4]]
    return reviews

def getUserReviews(cursor, userID):
    """
    Get the reviews made by a given user. Return a dictionary with the key being the review ids, and the values a list of the other elements.
    """
    cursor.execute('''
    SELECT * FROM reviews WHERE userID = %s;
    ''', (userID))
    rev_tup = cur.fetchall()
    reviews = {}
    for row in rev_tup:
        reviews[row[0]] = [row[1], row[2], row[3], row[4]]
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
            
            # Testing Edit Court
            # Call the editCourt function
            test_court2 = {
                "courtName": "New Court",
                "star": 5.0,
                "nets": 0,
                "level": 0,
                "clean": 0,
                "ada": 0,
                "inOut": 1,
                "hours": "Always",
                "price": "$5",
                "location": "123 Somewher Street",
            }
            print("\nTesting editCourt:")
            editCourt(cursor, court_id, test_court2["courtName"], test_court2["star"], test_court2["nets"], test_court2["level"], test_court2["clean"], test_court2["ada"], test_court2["inOut"], test_court2["hours"], test_court2["price"], test_court2["location"])
            print(f"Court edited with ID: {court_id}")
            
            court_details2 = getCourt(cursor, court_id)
            expected_result2 = (
                court_id,
                test_court2["courtName"],
                test_court2["star"],  # added a star value
                test_court2["nets"],
                test_court2["level"],
                test_court2["clean"],
                test_court2["ada"],
                test_court2["inOut"],
                test_court2["hours"],
                test_court2["price"],
                test_court2["location"],
            )
            assert court_details2 == expected_result2, f"Test failed: {court_details2} != {expected_result2}"
            print("editCourt test passed successfully.")
            
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