import db_setup as db 
import access_methods as acc

def initialize_db():
    """Initialise the database tables and insert initial data."""
    db.delete_tables()
    db.create_tables()
    acc.createCourt("Lakeshore Park Basketball Court", 4.5, 1, 1, 1, 1, 0, '10-18', '$5.99', 'Streeterville, Chicago', 'Nice indoor court')
    acc.createCourt("Douglas Park Outdoor Courts", 4, 0, 1, 1, 1, 1, '9-20', '$3.99', 'North Lawndale, Chicago', 'Most popular among locals')
    acc.createCourt("Margaret Hie Ding Lin Park Basketball Court", 5, 1, 0, 1, 0, 1, '11-19', '$4.00', 'Chinatown, Chicago', 'In a busy corner of Chinatown')
    acc.createCourt("Gill Park Basketball Court", 3, 1, 0, 1, 0, 1, '10-19', '$7.00', 'Lakeview East, Chicago', 'Expensive')
    print('Database loaded successfully')
    acc.addPhoto(1, "https://robbreport.com/wp-content/uploads/2022/03/200803_EJ_waterline_square-044944_HIGH_RES.jpg?w=1000")
    acc.addPhoto(2, "https://scissortailpark.org/wp-content/uploads/2022/10/306274736_807101607282596_7359110059786684243_n-1024x768.jpg")
    acc.addPhoto(3, "https://www.deckhouse.com/wp-content/uploads/2022/10/Acorn-Deck-House-prefab-custom-indoor-home-basketball-court-addition-7-scaled.jpg")
    acc.addPhoto(4, "https://www.sportcourtnortherncalifornia.com/wp-content/uploads/slider-basket-ball-court-putting-green.jpg")

if __name__ == '__main__':
    initialize_db()
