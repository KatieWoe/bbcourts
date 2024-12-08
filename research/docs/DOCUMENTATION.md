# Source Documentation

## Routes

- `/`: The landing page. Brief description of app and getting started.
- `/about`: A page that goes more into depth about the utility of the app.
- `/listing` Lists and links to all the courts currently in the database, including name, pic, and star rating.
- `/courts/<int:court_id>`: A dynamic page that takes the details of the court given and displays it with a number of reviews.

## Access Methods

- createCourt(courtName,avStar,nets,level,clean,ada,inOut,hours,price,location,description): Inserts a new court into the database and returns its ID.
- getCourts: Retrieve all courts. Returns a tuple with court ids.
- getCourt(courtID_get): Retrieve all details of a court by its ID. Returns a tuple with all court elements.
- calcAvStar(courtID_calc): Get the star rating from reviews for the court given. Calculate the average and return the average.
- editCourt(courtID_edit,courtName,avStar,nets,level,clean,ada,inOut,hours,price,location,description): Edit the court with the ID given so that all the parameters are now used.
- findCourts(search_term): Search the courts table in both the name and location atributes and return a list of IDs that pulled up matches.
- createReview(userID, courtID, star, comment): Create a review with a comment and a star review. Creates a random unique id. Returns that id.
- getReviews(courtID): Get the reviews for a given court. Returns a dictionary with the key being the review IDs, and the values a list of the other elements including the username, rating, and comment.
- getUserReviews(userID): Get the reviews made by a given user. Return a dictionary with the key being the review ids, and the values a list of the other elements.
- createUser(name, password): Inserts a new user into the database. Returns the userID of the created user.
- createUserFavorite(userID, courtID): Create a Favorite entry for the court belonging to the user. If the user has reviewed it, it records the star value. No return.
- getUserFavorites(userID): Get the users favorites based on id. Return as dictionary with key as courtID and star as the value.
- addPhoto(courtID, photo_path): Adds a photo to the photos table for a specific court. Returns the photoID of the newly added photo.
- getPhotos(courtID=None): Retrieves photos. If courtID is provided, retrieves photos for that court. Otherwise, retrieves all photos in the database. Returns a list of tuples containing photoID and photo paths.