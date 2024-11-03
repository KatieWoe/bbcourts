# Table #1: `courts`
* Table Description: 
* Fields:
   * `courtID`: Primary Key, Unique int to identify a court
   * `avStar`: Float holding the average star rating. Averages `star` values from Reviews with a matching `courtID`
   * `nets`: 0 or 1, Nets not present or present.
   * `level`: 0 or 1, Court doesn't or does have a level ground with no cracks.
   * `clean`: 0 or 1, Court is dirty or clean.
   * `ada`: 0 or 1, Court isn't or is accessable.
   * `inOut`: 0 or 1, Court is inside or outside.
   * `hours`: varchar, gives days and times the court is open.
   * `price`: varchar, gives price of admitance description
   * `location`: varchar, address of court
* List of tests for verifying each table:


# Table #2: `users`
* Name: 
* Table Description: 
* Fields:
   * `userID`: Primary Key, unique int to identify a user
   * `name`: varchar, user name of user
   * `password`: varchar, user password hashed
* List of tests for verifying each table:


# Table #3: `reviews`
* Name: 
* Table Description: 
* Fields:
   * `reviewID`: Primary Key, unique int to identify a review
   * `userID`: int, userID of review maker, matches `userID` in Users
   * `courtID`: int, courtID of court reviewed, matches `courtID` in Courts
   * `star`: float, 0-5 star rating given by the review
   * `comment`: varchar, written review
* List of tests for verifying each table:


# Table #4: `favorites` -- Jaekyeong Lee
* Name: 
* Table Description: 
* Fields:
   * `userID`: linked primary key with `courtID`, int that matches `userID` in Users
   * `courtID`: linked primary key with `userID`, int that matches `courtID` in Courts
   * `review`: float or null, matches `star` from Reviews if user has reviewed this court
* List of tests for verifying each table:


# Table #5: `photos` (?)
* Name: 
* Table Description: 
* Fields:
   * `photoID`: Primary Key, unique int to identify a picture
   * `courtID`: int, courtID of court pictured, matches `courtID` in Courts
   * `photo`: varchar, link to photo
* List of tests for verifying each table:


# Data Access Method #1 -- Jaekyeong Lee
* Name:
* Description:
* Parameters:
* Return values:
* List of tests for verifying each access method:


# Data Access Method #2
* Name:
* Description:
* Parameters:
* Return values:
* List of tests for verifying each access method:


# Data Access Method #3
* Name:
* Description:
* Parameters:
* Return values:
* List of tests for verifying each access method:


# Data Access Method #4
* Name:
* Description:
* Parameters:
* Return values:
* List of tests for verifying each access method:


# Data Access Method #5
* Name:
* Description:
* Parameters:
* Return values:
* List of tests for verifying each access method:

...



# Questions to consider (To be removed before submission)
* What are the constraints for those table fields?
* What are the relationships between tables?
* What are the functions that will be created to access the database?
* What are the tests to make sure those access routines work?
* Which pages will need to access the database information?
* What are the tests to make sure the pages access the correct data in the database?
