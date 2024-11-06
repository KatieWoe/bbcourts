# Table #1: `courts`
* Table Description: This table holds the information about a given basketball court, including average reviews. It will be accessed by the Landing page to display a random court, the Search Results to find entries that have a match in courtName or location to the search results and display the information of those matched courts, the Court Details page to display all of a court's details, the Make a Review page to provide a matching courtID to the court being reviewed and to update the avStar value after a review is finished, and the Favorites page to display the court info of courtID's that match a user's favorites.
* Fields:
   * `courtID`: Primary Key, Unique int to identify a court
   * `courtName`: varchar, gives a name for the court
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
    * Test adding good entry with all "false"
        * nets, level, clean, ada, and inOut should all be tested with a value of 0 at least once, should succeed
        * courtID should be int, courtName should be varchar, avStar should be calculated and either 0-5 or null, hours, price, and location should be varchar
    * Test adding good entry with all "true"
        * nets, level, clean, ada, and inOut should all be tested with a value of 1 at least once, should succeed
        * courtID should be int, courtName should be varchar, avStar should be calculated and either 0-5 or null, hours, price, and location should be varchar
    * Test adding wrong type or not constrained values for all elements/Test adding empty string and/or null for all elements
        * courtID tested with non int and null values, should throw error
        * courtName tested with empty string, non-varchar, and null values, should throw error
        * nets, level, clean, ada, and inOut should all be tested with non int and non 0 or 1, should throw error
        * nets, level, clean, ada, and inOut should all be tested with null, should succeed
        * hours, price, and location should all be tested with non-varchar and null values, should throw error
        * hours, price, and location should all be tested with empty string, should succeed
    * Test that adding an entry in `reviews` with matching courtID updates avStar
        * Add entries to reviews before court made, should throw error
        * Add entries to reviews after court made, avStar should update (this will be done when entering review)
    * Test good changes to each element
        * Changes should be correct type, in constraints, and null if allowed, see good entry tests
    * Test wrong type or not constrained values changes for all elements
        * Changes should be wrong types, not constrained, and null if not allowed, see adding bad entry tests
    * Test adding new entry with elements that are duplicated in previous entries
        * Duplicate courtID should throw error, all other entries should succeed
    * Test deleting an entry
        * Should succeed
    


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
