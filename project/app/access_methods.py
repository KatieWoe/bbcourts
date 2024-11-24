import psycopg2
import random

def createCourt(connection, courtName, nets, level, clean, ada, inOut, hours, price, location):
    """
    Input the parameters into a new court, generate a new iD, and return the ID. Average star starts as null.
    """
    cur = connection.cursor()
    """
    cur.execute('''
    SELECT courtID FROM courts;
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
    INSERT INTO courts VALUES (?, NULL, ?, ?, ?, ?, ?, ?, ?, ?) RETURNING courtID;
    ''', (courtName, nets, level, clean, ada, inOut, hours, price, location))
    id_of_new_row = cur.fetchone()[0]
    
    connection.commit()
    connection.close()
    return id_of_new_row

def deleteCourt(connection, courtID_del):
    """
    Delete the court with the id given.
    """
    cur = connection.cursor()
    cur.execute('''
    DELETE FROM courts WHERE courtID=?;
    ''', (courtID_del))
    connection.commit()
    connection.close()
    return

def getCourt(connection, courtID_get):
    """
    Select everything from the court with the given id. Returns a tupple with all elements.
    """
    cur = connection.cursor()
    cur.execute('''
    SELECT * FROM courts WHERE courtID=?;
    ''', (courtID_get))
    court_tup = cur.fetchall()
    court = court_tup[0]
    connection.commit()
    connection.close()
    return court

def calcAvStar(connection, courtID_calc):
    """
    Get the star rating from reviews for the court given. Calculate the average and return the average.
    """
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
