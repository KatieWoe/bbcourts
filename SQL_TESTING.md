# Table #1: `courts` -- Katie
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
    * Test that avStar is calculated correctly
        * No reviews for a court should give a null avStar
        * Add entries to reviews after court made, updating avStar should give correct average based on those reviews
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


# Table #3: `reviews` -- Jonathan
* Table Description: This table holds individual reviews submitted by users for basketball courts. It will be accessed by the Court Details page to display reviews for each court, the User Profile page to show reviews made by a user, and the Make a Review page to save user-generated reviews. The `star` field contributes to calculating the `avStar` in the `courts` table, updating the average rating for the corresponding court after each new review is added.
* Fields:
   * `reviewID`: Primary Key, unique int to identify a review
   * `userID`: int, identifies the user who made the review, matches `userID` in the `Users` table
   * `courtID`: int, identifies the court being reviewed, matches `courtID` in the `courts` table
   * `star`: Float, holds a 0-5 star rating given by the review
   * `comment`: varchar, holds the written review content

* List of tests for verifying each table:
    * **Test adding a valid entry**
        * Valid entry should succeed with an integer `reviewID`, `userID`, and `courtID`, a `star` rating between 0 and 5, and a varchar `comment`.
    * **Test adding a review with all minimum values**
        * `star` is 0, and `comment` is an empty string. Should succeed as 0 is within valid rating range, and an empty `comment` is allowed.
    * **Test adding a review with all maximum values**
        * `star` is 5, `comment` reaches the maximum allowed varchar length (based on system limits). Should succeed if within varchar constraints.
    * **Test adding invalid values**
        * Adding non-integer or null values for `reviewID`, `userID`, or `courtID` should throw an error.
        * Adding a `star` rating outside the 0-5 range (e.g., -1, 6) should throw an error.
        * Adding a non-varchar type to `comment` should throw an error; null or empty string should succeed.
    * **Test updating a review**
        * Modifying `star` or `comment` fields with valid data should succeed.
        * Modifying `userID` or `courtID` should not affect the `courts` or `users` table integrity and should succeed if values exist in the `users` and `courts` tables.
    * **Test deleting a review**
        * Deleting a review should remove it from the table and trigger recalculation of `avStar` in the `courts` table if applicable.




# Table #4: `favorites` -- Jaekyeong Lee
* Table Description: The 'Favorites' page will query this table to display the courts favorited by the user. Each row in the table represents a court (identified by `courtID`) that a specific user (identified by `userID`) has favorited. The table also includes a review field to show the user's star rating for the court, if available.
* Fields:
   * `userID`: linked primary key with `courtID`, int that matches `userID` in Users
   * `courtID`: linked primary key with `userID`, int that matches `courtID` in Courts
   * `review`: float or null, matches `star` from Reviews if user has reviewed this court
* List of tests for verifying each table:
  * Testing that (`userID`, `courtID`) is unique. The combination of userID and courtID should be unique in the table as a user can favourite each court only once.
  * Testing that (`userID`, `courtID`) allows no null values
  * Testing that `userID` matches a valid `userID` in the `users` table.
  * Testing that `courtID` matches a valid `courtID` in the `courts` table
  * Testing that `review` field accepts valid float values.
  * Testing that `review` field accepts null values.
  * Testing adding a favourite court without a review.
  * Testing updating `review`. If a user adds a review for a court they’ve favourited, verify that the `review` field in `favourites` updates to reflect the new rating.
  * Testing deleting a favourite
  * Testing that querying favourited courts by userID returns the correct list of `courtID`s


# Table #5: `photos` -- Jonathan
* Table Description: This table stores photos associated with each basketball court. It will be accessed by the Court Details page to display images of the court, providing the user's with an overview of what the court looks like. The `courtID` field links each photo to a specific court in the `courts` table.
* Fields:
   * `photoID`: Primary Key, unique int to identify a picture
   * `courtID`: int, identifies the court being pictured, matches `courtID` in the `courts` table
   * `photo`: varchar, holds a link or path to the photo

* List of tests for verifying each table:
    * **Test adding a valid entry**
        * Valid entry should succeed with an integer `photoID`, integer `courtID`, and a valid `photo` link as varchar.
    * **Test adding photo with all minimum values**
        * `photo` is an empty string. Should succeed, as an empty `photo` link is allowed.
    * **Test adding photo with all maximum values**
        * `photo` reaches the maximum allowed varchar length. Should succeed if within varchar constraints.
    * **Test adding invalid values**
        * Adding non-integer or null values for `photoID` or `courtID` should throw an error.
        * Adding a non-varchar type to `photo` should throw an error; null or empty string should succeed.
    * **Test updating a photo entry**
        * Modifying `photo` with a valid link or path should succeed.
        * Changing `courtID` should maintain linkage to a valid court in the `courts` table.
    * **Test deleting a photo entry**
        * Deleting a photo entry should succeed, and the image should no longer display on the Court Details page if linked to a deleted court.

# Data Access Method #1 -- Jaekyeong Lee
* Name: `getUserFavorites`
* Description: retrieves the list of courts favourited by a specified user from the `favorites` table. This method is intended to populate the 'Favorites' page, displaying favourited courts and associated star ratings for the user.
* Parameters
  * `userID` (int): The unique identifier of the user logged in. Must match an existing `userID` in the `users` table.
* Return values:
  * Returns a dictionary with
    * key: courtID (int). The unique identifier of the favourited court.
    * value: review (float or null). The star rating the user has given to the court, if available, otherwise, null.

  * If the `userID` does not exist or if no favourites are found for the given user, it returns an empty dictionary.
* List of tests for verifying each access method:
  * Test retrieving favourites for a valid `userID` that has favourited courts.
  * Test retrieving favourites for a valid `userID` that has not favourited any courts.
  * Test retrieving favourites for a `userID` that does not exist in the Users table
  * Test that the method handles entries with null review values correctly.
  * Test retrieving favourites with rating.


# Data Access Method #2 -- Katie
* Name: createCourt
* Description: Create a new entry in courts table.
* Parameters: courtName(str), nets(0,1), level(0,1), clean(0,1), ada(0,1), inOut(0,1), hours(str), price(str), location(str)
* Return values: courtID (a unique and randomized int that was assigned to the court)
* List of tests for verifying each access method:
    * For good inputs: Search for returned courtID and make sure inputs match result and avStar is null
    * For bad inputs: Throw an error


# Data Access Method #3 -- Katie
* Name: deleteCourt
* Description: Delete an existing entry in courts table
* Parameters: courtID(int)
* Return values: None
* List of tests for verifying each access method:
    * For good inputs: Search for courtID should come back with no results
    * For bad inputs or courtID does not exist: Throw an error


# Data Access Method #4 -- Katie
* Name: getCourt
* Description: Gets all the info in a courts entry so it can be displayed on page. How much of the returned data is used depends on what the function call is used for. For example, it can be used to access the loation info to get map and weather data if you only access the location element of the returned tuple.
* Parameters: courtID(int)
* Return values: courtName(str), avStar(float), nets(0,1), level(0,1), clean(0,1), ada(0,1), inOut(0,1), hours(str), price(str), location(str)
* List of tests for verifying each access method:
    * For existing court: returned values should match values gotten when you Search for that courtID in courts
    * For bad input: throw error
    * For non-existing court: throw error


# Data Access Method #5 -- Toan 
* Name: editCourt
* **Description**: Stores information on basketball courts, including details like location, amenities, and ratings. Used across: Landing Page, Search Results, Court Details Page, Make a Review Page, Favorites Page
* **Fields**:
   - `courtID`: **Primary Key**, unique int for each court.
   - `courtName`: **varchar**, court's name.
   - `avStar`: **Float**, average rating from related reviews.
   - `nets`, `level`, `clean`, `ada`, `inOut`: **0 or 1**, represent amenities and features (e.g., ADA access).
   - `hours`, `price`, `location`: **varchar**, court availability, admission price, and address.

* **Tests**:
   - **Valid Entries**:
     - Add entries with all fields as 0 or 1. Ensure field types match and constraints hold.

   - **Invalid Entries**:
     - Test invalid `courtID` (non-int/null), `courtName` (empty string/non-varchar/null), and boolean fields with values other than 0 or 1. Ensure errors are thrown.
     - Confirm `nets`, `level`, `clean`, `ada`, `inOut` accept null, and `hours`, `price`, `location` accept empty strings but not null.

   - **`avStar` Calculation**:
     - Ensure `avStar` is null with no reviews and updates correctly with added reviews.

   - **Updating Fields**:
     - Test valid updates to all fields; ensure changes apply. Confirm errors on invalid updates.

   - **Duplicate and Delete**:
     - Test duplicate `courtID` (error expected), other fields (allowed).
     - Delete entry and confirm removal from search results.

...



# Questions to consider (To be removed before submission)
* What are the constraints for those table fields?
* What are the relationships between tables?
* What are the functions that will be created to access the database?
* What are the tests to make sure those access routines work?
* Which pages will need to access the database information?
* What are the tests to make sure the pages access the correct data in the database?
