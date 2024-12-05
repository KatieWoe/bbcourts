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
    acc.addPhoto(1, "https://assets-global.website-files.com/6173bb4ce523620d28c5c2d3/6174a0fd5b9a2b5471172a89_Hoop-City-Full-Court.jpg")
    acc.addPhoto(1, "https://nevco.com/wp-content/uploads/2021/02/750-Basketball-600x0-c-default.jpg")
    acc.addPhoto(1, "https://images.dickssportinggoods.com/marketing/DSG_TMS_Basketball_8333984_CLP_Basketball_11_3_2024_s31031142950.jpg")
    
    acc.addPhoto(2, "https://scissortailpark.org/wp-content/uploads/2022/10/306274736_807101607282596_7359110059786684243_n-1024x768.jpg")
    acc.addPhoto(2, "https://storage.googleapis.com/proudcity/santaanaca/uploads/2022/03/basketball-courts-at-memorial-park.jpg")
    acc.addPhoto(2, "https://www.tustinca.org/ImageRepository/Document?documentID=3968")
    acc.addPhoto(2, "https://images.squarespace-cdn.com/content/v1/58b72cc520099eaff33166ea/1687987226768-KVA5GMWK4H66QXA8Q1OJ/DJI_0133+%281%29.JPG")
    
    acc.addPhoto(3, "https://www.deckhouse.com/wp-content/uploads/2022/10/Acorn-Deck-House-prefab-custom-indoor-home-basketball-court-addition-7-scaled.jpg")
    acc.addPhoto(3, "https://cdn.sqhk.co/2020newsportcourt/2020/3/geijeid/IMG_0240.JPG")
    acc.addPhoto(3, "https://st.hzcdn.com/simgs/pictures/home-gyms/indoor-home-basketball-court-groom-construction-co-inc-img~43e16aa409025659_14-1782-1-a57cb85.jpg")
    acc.addPhoto(3, "https://i.pinimg.com/236x/48/9b/5e/489b5ec4a8e89bdf35247ece508203d2.jpg")
    
    acc.addPhoto(4, "https://www.sportcourtnortherncalifornia.com/wp-content/uploads/slider-basket-ball-court-putting-green.jpg")
    acc.addPhoto(4, "https://sportcourt.ca/wp-content/uploads/2019/04/mertesky-toronto-28x40-1024x765.jpg")
    acc.addPhoto(4, "https://sportcourt.ca/wp-content/uploads/2019/04/mandel-g-north-york-1024x768.jpg")
    acc.addPhoto(4, "https://img.posterstore.com/zoom/ps52266.jpg?auto=compress%2Cformat&fit=max&w=3840")
    
    acc.addPhoto(5, "https://www.ymcalouisville.org/sites/default/files/2021-12/ymca-louisville-northeast-branch-5.jpg")
    acc.addPhoto(5, "https://www.ymcawf.org/images/images/DSC00018_med.jpg")
    acc.addPhoto(5, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4ZAVWWAI3GZ2PeT8ffQgEjVXr9VspX3Qqyg&s")
    acc.addPhoto(5, "https://ymcaboston.org/wp-content/uploads/2021/07/gymnasium-2.jpg")
    

if __name__ == '__main__':
    initialize_db()
