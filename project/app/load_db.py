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
    acc.createCourt("YMCA of Freeport", 3.5, 1, 1, 1, 0, 0, '8-7', 'Membership', 'Highland, Freeport', 'The court at the local YMCA. It is part of the Highland college campus. The membership fee is typical of YMCA but if you are a student at the college you get a free membership. Great way to spend time between class.')
    acc.createCourt("Backyard Ball", 1.5, 0, 0, 0, 0, 1, 'Always', 'Free', 'Nowhere, Good', 'RUN! It is free and always open, but I have never seen a more rundown court in my life. It smells like fish and is always cold for some reason, even in the summer.')
    acc.createCourt("Waneka Lake", 4.5, 0, 1, 1, 0, 1, 'Always', 'Free', 'Lafayet, CO', 'A lovely court next to Waneka lake. Well maintained and only a short walk from the play park. The lighting is not the best durring the fall when it gets dark out, but during the summer it is the best spot.')
    acc.createCourt("Eagle Park Place", 3, 1, 1, 1, 0, 0, 'Weekends', '$2', 'Downtown, Shannon', 'A nice enough park but very out of the way. A 10 minute walk from the parking lot and so many stairs to get there that it is not at all accessible. Only open on weekends.')
    acc.createCourt("Dream Yard Court", 4, 1, 1, 1, 1, 0, '9-5', '$6', 'Fancy, Place', 'Rather overblown. Very popular, but overpriced and only open during buisnes hours. Has a fun pick up game scene, but only in the summer and mostly rich kids frequent it.')
    acc.createCourt("Play Place", 5, 1, 1, 1, 1, 1, '9-5', 'Free', 'Fancy, Place', 'A kid only court that holds lessons for beginers. Free for kids under 10 and their parents. A lovely, low stress place for kids to play.')
    print('Database loaded successfully')
    
    acc.addPhoto(1, "https://robbreport.com/wp-content/uploads/2022/03/200803_EJ_waterline_square-044944_HIGH_RES.jpg?w=1000")
    acc.addPhoto(2, "https://scissortailpark.org/wp-content/uploads/2022/10/306274736_807101607282596_7359110059786684243_n-1024x768.jpg")
    acc.addPhoto(3, "https://www.deckhouse.com/wp-content/uploads/2022/10/Acorn-Deck-House-prefab-custom-indoor-home-basketball-court-addition-7-scaled.jpg")
    acc.addPhoto(4, "https://www.sportcourtnortherncalifornia.com/wp-content/uploads/slider-basket-ball-court-putting-green.jpg")

if __name__ == '__main__':
    initialize_db()
