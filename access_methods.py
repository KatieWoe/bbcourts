import psycopg2
from random import randint

def createCourt(connection, courtName, nets, level, clean, ada, inOut, hours, price, location):
    cur = connection.cursor()
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
    
    cur.execute('''
    INSERT INTO courts(maybe_id, courtName, NULL, nets, level, clean, ada, inOut, hours, price, location);
    ''')
    connection.commit()
    connection.close()
    return maybe_id

def deleteCourt(courtID_del):
    cur = connection.cursor()
    cur.execute('''
    DELETE FROM courts WHERE courtID=courtID_del;
    ''')
    connection.commit()
    connection.close()
    return

def getCourt(courtID_get):
    cur = connection.cursor()
    cur.execute('''
    SELECT * FROM courts WHERE courtID=courtID_get;
    ''')
    court_tup = cur.fetchall()
    court = court_tup[0]
    connection.commit()
    connection.close()
    return court