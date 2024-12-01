import psycopg2
import random

DATABASE_URL = "postgresql://jjjohnywaffles_k8io_user:vaeBbrGmOq2g6GVR7zttI2g2bsf7Gh8f@dpg-ct1nsddumphs738rb1f0-a.oregon-postgres.render.com/jjjohnywaffles_k8io"

def createCourt(cursor, courtName, nets, level, clean, ada, inOut, hours, price, location, description):
    """
    Inserts a new court into the database and returns its ID.
    """
    cursor.execute('''
        INSERT INTO courts (courtName, avStar, nets, level, clean, ada, inOut, hours, price, location, description)
        VALUES (%s, NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING courtID;
    ''', (courtName, nets, level, clean, ada, inOut, hours, price, location, description))
    court_id = cursor.fetchone()[0]
    return court_id

"""
def createCourt(courtName, nets, level, clean, ada, inOut, hours, price, location):
    connection = psycopg2.connect(DATABASE_URL)
    try:
        with connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO courts (courtName, avStar, nets, level, clean, ada, inOut, hours, price, location, description)
                VALUES (%s, NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING courtID;
            ''', (courtName, nets, level, clean, ada, inOut, hours, price, location, description))
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

def editCourt(cursor, courtID_edit, courtName, avStar, nets, level, clean, ada, inOut, hours, price, location, description):
    """
    Edit the court with the ID given so that all the parameters are now used.
    """
    cursor.execute('''
    UPDATE courts SET courtName=%s, avStar=%s, nets=%s, level=%s, clean=%s, ada=%s, inOut=%s, hours=%s, price=%s, location=%s, description=%s WHERE courtID=%s;
    ''', (courtName, avStar, nets, level, clean, ada, inOut, hours, price, location, description, courtID_edit))
    return

def findCourts(cursor, search_term):
    """
    Search the courts table in both the name and location atributes and return a list of IDs that pulled up matches.
    """
    cursor.execute(f"""
    SELECT courtID FROM courts WHERE courtName LIKE '%{search_term}%';
    """)
    names_tup = cursor.fetchall()
    names = []
    for row in names_tup:
        names.append(row[0])
    cursor.execute(f"""
    SELECT courtID FROM courts WHERE location LIKE '%{search_term}%';
    """)
    loc_tup = cursor.fetchall()
    locs = []
    for row in loc_tup:
        locs.append(row[0])
    bothlists = list(set(names) | set(locs))
    return bothlists

def createReview(cursor, userID, courtID, star, comment):
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
    id_of_new_row = cursor.fetchone()[0]
    
    return id_of_new_row

def getReviews(cursor, courtID):
    """
    Get the reviews or a given court. Returns a dictionary with the key being the review ids, and the values a list of the other elements.
    """
    cursor.execute('''
    SELECT * FROM reviews WHERE courtID = %s;
    ''', (courtID,))
    rev_tup = cursor.fetchall()
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
    ''', (userID,))
    rev_tup = cursor.fetchall()
    reviews = {}
    for row in rev_tup:
        reviews[row[0]] = [row[1], row[2], row[3], row[4]]
    return reviews

def deleteReview(cursor, reviewID_del):
    """
    Delete a review using the reviewID)
    """
    cursor.execute('''
        DELETE FROM reviews WHERE reviewID = %s;
    ''', (reviewID_del,))
    return

# CreateUser Method
def createUser(cursor, name, password):
    """
    Inserts a new user into the database.
    Returns the userID of the created user.
    """
    try:
        cursor.execute('''
            INSERT INTO users (name, password)
            VALUES (%s, %s)
            RETURNING userID;
        ''', (name, password))
        user_id = cursor.fetchone()[0]
        return user_id
    except psycopg2.IntegrityError as e:
        raise ValueError(f"User with name '{name}' already exists.") from e

# Checks to see User
def checkUser(cursor, name, password):
    """
    Checks if a user exists with the given name and password.
    Returns the userID if the user exists, otherwise None.
    """
    cursor.execute('''
        SELECT userID FROM users
        WHERE name = %s AND password = %s;
    ''', (name, password))
    result = cursor.fetchone()
    return result[0] if result else None      

def createUserFavorite(cursor, userID, courtID):
    """
    Create a Favorite entry for the court belonging to the user. If the user has reviewed it, it records the star value. No return.
    """
    reviews = getUserReviews(cursor, userID)
    review_for_court = None
    for key in reviews:
        if reviews[key][2] != None:
            review_for_court = reviews[key][2]
    if review_for_court != None:
        cursor.execute('''
        INSERT INTO favorites (userID, courtID, review) VALUES (%s, %s, %s)
        ''', (userID, courtID, review_for_court))
    else:
        cursor.execute('''
        INSERT INTO favorites (userID, courtID) VALUES (%s, %s)
        ''', (userID, courtID))
    return

def getUserFavorites(cursor, userID):
    """
    Get the users favorites based on id. Return as dictionary with key as courtID and star as the value.
    """
    cursor.execute('''
    SELECT * FROM favorites WHERE userID = %s;
    ''', (userID,))
    fav_tup = cursor.fetchall()
    favorites = {}
    for row in fav_tup:
        favorites[row[1]] = row[2]
    return favorites
    

def editUserFavorite(cursor, userID, courtID, star):
    """
    Edit a users favorite entry to include a star value if they reviewed after favoriting.
    """
    cursor.execute('''
    UPDATE favorites SET review=%s WHERE courtID=%s AND userID=%s;
    ''', (star, courtID, userID))
    return

def deleteUserFavorite(cursor, userID, courtID):
    """
    Delete a users favorite based on the userid and courtid.
    """
    cursor.execute('''
        DELETE FROM favorites WHERE userID = %s AND courtID = %s;
    ''', (userID, courtID))
    return
    

# Adding Photo
def addPhoto(cursor, courtID, photo_path):
    """
    Adds a photo to the photos table for a specific court.
    Returns the photoID of the newly added photo.
    """
    cursor.execute('''
        INSERT INTO photos (courtID, photo)
        VALUES (%s, %s)
        RETURNING photoID;
    ''', (courtID, photo_path))
    photo_id = cursor.fetchone()[0]
    return photo_id

# Getting a Specific User
def getUser(cursor, userID):
    """
    Retrieves a user by their userID.
    Returns a tuple containing the user's details (userID, name, password).
    """
    cursor.execute('''
        SELECT * FROM users
        WHERE userID = %s;
    ''', (userID,))
    user = cursor.fetchone()
    return user

# Getting photo
def getPhotos(cursor, courtID=None):
    """
    Retrieves photos.
    If courtID is provided, retrieves photos for that court.
    Otherwise, retrieves all photos in the database.
    Returns a list of tuples containing photoID and photo paths.
    """
    if courtID:
        cursor.execute('''
            SELECT photoID, photo FROM photos
            WHERE courtID = %s;
        ''', (courtID,))
    else:
        cursor.execute('''
            SELECT photoID, photo FROM photos;
        ''')
    photos = cursor.fetchall()
    return photos

# Deleting User
def deleteUser(cursor, userID):
    """
    Deletes a user by their userID.
    """
    cursor.execute('''
        DELETE FROM users
        WHERE userID = %s;
    ''', (userID,))
    print(f"User with ID {userID} deleted successfully.")

# Deleting Photo
def deletePhoto(cursor, photoID):
    """
    Deletes a photo by its photoID.
    """
    cursor.execute('''
        DELETE FROM photos
        WHERE photoID = %s;
    ''', (photoID,))
    print(f"Photo with ID {photoID} deleted successfully.")

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
                "description": "test description"
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
                test_court["description"]
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
                test_court["description"]
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
                "location": "123 Somewhere Street",
                "description": "other describe"
            }
            print("\nTesting editCourt:")
            editCourt(cursor, court_id, test_court2["courtName"], test_court2["star"], test_court2["nets"], test_court2["level"], test_court2["clean"], test_court2["ada"], test_court2["inOut"], test_court2["hours"], test_court2["price"], test_court2["location"], test_court2["description"])
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
                test_court2["description"]
            )
            assert court_details2 == expected_result2, f"Test failed: {court_details2} != {expected_result2}"
            print("editCourt test passed successfully.")
            
            # Testing Search
            print("\nTesting findCourts:")
            search_results = findCourts(cursor, "Somewhere")
            assert court_id in search_results, f"Test failed: {court_id} not in {search_results}"
            print("findCourts passed successfully")
            
            
            # TESTING REVIEWS
            # Create 3 reviews
            test_review_1 = {
                "userID": 9, 
                "courtID": court_id, 
                "star": 5.0, 
                "review": "test review"
            }
            test_review_2 = {
                "userID": 11, 
                "courtID": court_id, 
                "star": 4.0, 
                "review": "another test"
            }
            
            
            print("\nTesting createReview:")
            review1id = createReview(cursor, test_review_1["userID"], test_review_1["courtID"], test_review_1["star"], test_review_1["review"])
            print(f"Review created with ID: {review1id}")
            review2id = createReview(cursor, test_review_2["userID"], test_review_2["courtID"], test_review_2["star"], test_review_2["review"])
            print(f"Review created with ID: {review2id}")
            print("createReview passed successfully")
            
            # Testing Average Star
            print("\nTesting calcAvStar:")
            test_average = calcAvStar(cursor, court_id)
            assert test_average == 4.5, f"Test failed: {test_average} != 4.5"
            print("calcAvStar passed successfully")
            
            # Testing Get Review
            print("\nTesting getReviews:")
            court_reviews = getReviews(cursor, court_id)
            assert court_reviews[review1id] == [test_review_1["userID"], test_review_1["courtID"], test_review_1["star"], test_review_1["review"]], f"Test failed: Review {review1id} wrong"
            print("getReviews passed successfully")
            
            # Testing Get Users Review
            print("\nTesting getUserReviews:")
            court_reviews = getUserReviews(cursor, 11)
            assert court_reviews[review2id] == [test_review_2["userID"], test_review_2["courtID"], test_review_2["star"], test_review_2["review"]], f"Test failed: Review {review2id} wrong"
            print("getUserReviews passed successfully")
            
            #Test Create and Get Favorites
            print("\nTesting createUserFavorite:")
            createUserFavorite(cursor, 9, court_id)
            print("User Favorite Created")
            userFave = getUserFavorites(cursor, 9)
            assert userFave[court_id] == 5.0, f"Test failed: User Favorite for User9 and {court_id} is {userFave[court_id]} instead of 5.0"
            print("create and get UserFavorite passed successfully")
            
            # Delete Reviews
            print("\nTesting deleteReview:")
            deleteReview(cursor, review1id)
            print(f"Review with ID {review1id} deleted successfully.")
            deleteReview(cursor, review2id)
            print(f"Review with ID {review2id} deleted successfully.")
            
            
            # Verify the reviews no longer exists
            cursor.execute("SELECT * FROM reviews WHERE reviewID = %s;", (review1id,))
            deleted_review1 = cursor.fetchone()
            assert deleted_review1 is None, f"Test failed: Review with ID {review1id} still exists."
            cursor.execute("SELECT * FROM reviews WHERE reviewID = %s;", (review2id,))
            deleted_review2 = cursor.fetchone()
            assert deleted_review2 is None, f"Test failed: Review with ID {review2id} still exists."
            print("deleteReview test passed successfully.")
            
            
            # Test no star favorite get
            print("\nTesting getUserFavorite with no star:")
            createUserFavorite(cursor, 12, court_id)
            print("User Favorite Created No Star")
            userFave2 = getUserFavorites(cursor, 12)
            assert userFave2[court_id] == None, f"Test failed: User Favorite for User12 and {court_id} is {userFave2[court_id]} instead of None"
            createUserFavorite(cursor, 11, court_id)
            print("User Favorite Created No Star")
            userFave3 = getUserFavorites(cursor, 11)
            assert userFave3[court_id] == None, f"Test failed: User Favorite for User11 and {court_id} is {userFave3[court_id]} instead of None"
            print("getUserFavorites passes with null star")
            
            # Test Delete Favorite
            print("\nTesting deleteUserFavorite:")
            deleteUserFavorite(cursor, 9, court_id)
            print("Favorite Deleted Successfully")
            cursor.execute("SELECT * FROM favorites WHERE userID = 9 AND courtID = %s;", (court_id,))
            deleted_fave = cursor.fetchone()
            assert deleted_fave is None, "Test failed: Favorite still exists."
            deleteUserFavorite(cursor, 12, court_id)
            print("Favorite Deleted Successfully")
            cursor.execute("SELECT * FROM favorites WHERE userID = 12 AND courtID = %s;", (court_id,))
            deleted_fave2 = cursor.fetchone()
            assert deleted_fave2 is None, "Test failed: Favorite still exists."
            deleteUserFavorite(cursor, 11, court_id)
            print("Favorite Deleted Successfully")
            cursor.execute("SELECT * FROM favorites WHERE userID = 11 AND courtID = %s;", (court_id,))
            deleted_fave3 = cursor.fetchone()
            assert deleted_fave3 is None, "Test failed: Favorite still exists."
            
            
            # TESTING DELETE Court
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