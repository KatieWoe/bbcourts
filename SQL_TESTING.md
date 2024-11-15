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
* Table Description: This table holds all information related to users of the website. It will be used to save information on user reviews, and favorited courts for each user. The website will have a login page where users enter their credentials. The login page will also have a user signup prompt, where user records will be generated and saved into this table. Once a user is logged in, they can view which courts they have reviewed in the Favorites page, as well as which courts they have favorited in the same page. Within the Court Details page, users will have access to the review function via the "Submit your rating" section, where they can assign a star rating and submit a review. Once they hit the submit button, they will be taken to the Make a Review page, where they can submit reviews for each court. The `userID` key is referenced in the `reviews` and `favorites` table to allow the application to determine which reviews belong to which user and display this information in the relevant sections of the website. 
* Fields:
   * `userID`: Primary Key, unique int to identify a user
   * `name`: varchar, user name of user
   * `password`: varchar, user password hashed
* List of tests for verifying each table:
    * Testing valid entry on signup: The username (`name`) should be unique, and the `password` will have to satisfy a set of requirements to ensure security.
    * Testing primary key: The primary key `userID` should satisfy all of the requirements for a primary key, including uniqueness, non-nullness, stability, and simplicity.
    * Testing invalid entries on signup:
        * Non-unique username: `name` should be unique to each user. We must test whether the `name` that a user chooses as their username is not already taken.
        * Invalid password: `password` should meet our set of requirements for security. We will validate the password to check if it meets our criteria (ex. length > 12 characters, combination of uppercase, lowercase, numbers, special characters)
    * Testing valid entries on login: When a user logs in with their credentials, we must test whether their username and password exist in our database, and verify that matching credentials will yield a successful login.
    * Testing invalid entries on login: If the user attempts to log in with an invalid `name` or `password`, we must test that a check against the database yields the correct result (denial of login), and test that the correct prompt is returned to the user.
    * Testing review functionality: We must test that a successfully logged in user can submit reviews, and view/edit their reviews in the Court listings and Favorites pages
    * Testing favorites functionality: We must test that a successfully logged in user can favorite a court, and that the favorited courts appear in both the Court listings (as a heart), and the Favorites page


# Table #3: `reviews` 
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




# Table #4: `favorites` 
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


# Table #5: `photos` 
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

# Data Access Method #1 
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
  
# Data Access Method #2
* Name: `createUserFavorites`
* Description: makes a new favourited by a specified user from the `favorites` table. This method is intended to create a new entry in the 'Favorites' page, displaying favourited courts and associated star ratings for the user.
* Parameters
  * `userID` (int): The unique identifier of the user logged in. Must match an existing `userID` in the `users` table.
  * `courtID` (int): The id of the court being favorited. Must match an existing `courtID` in `courts` table.
* Return values:
  * Returns None

* List of tests for verifying each access method:
  * Test making favourites for a valid `userID` and `courtID`
  * Test making favourites for a valid `userID` but not `courtID`, should throw error
  * Test making favourites for a `userID` that does not exist in the Users table, should throw error

# Data Access Method #3
* Name: `deleteUserFavorites`
* Description: Removes a favorited court when user chooses to remove (from court listing page or Favorites page)
* Parameters
  * `userID` (int): The unique identifier of the user logged in. Must match an existing `userID` in the `users` table.
  * `courtID` (int): The id of the court being favorited. Must match an existing `courtID` in `courts` table.
* Return values:
  * Returns None

* List of tests for verifying each access method:
  * Test removing favourites for a valid `userID` and `courtID`
  * Test removing favourites for a valid `userID` but not `courtID`, should throw error
  * Test removing favourites for a `userID` that does not exist in the Users table, should throw error

# Data Access Method #4
* Name: createCourt
* Description: Create a new entry in courts table.
* Parameters: courtName(str), nets(0,1), level(0,1), clean(0,1), ada(0,1), inOut(0,1), hours(str), price(str), location(str)
* Return values: courtID (a unique and randomized int that was assigned to the court)
* List of tests for verifying each access method:
    * For good inputs: Search for returned courtID and make sure inputs match result and avStar is null
    * For bad inputs: Throw an error


# Data Access Method #5
* Name: deleteCourt
* Description: Delete an existing entry in courts table
* Parameters: courtID(int)
* Return values: None
* List of tests for verifying each access method:
    * For good inputs: Search for courtID should come back with no results
    * For bad inputs or courtID does not exist: Throw an error


# Data Access Method #6
* Name: getCourt
* Description: Gets all the info in a courts entry so it can be displayed on page. How much of the returned data is used depends on what the function call is used for. For example, it can be used to access the loation info to get map and weather data if you only access the location element of the returned tuple.
* Parameters: courtID(int)
* Return values: courtName(str), avStar(float), nets(0,1), level(0,1), clean(0,1), ada(0,1), inOut(0,1), hours(str), price(str), location(str)
* List of tests for verifying each access method:
    * For existing court: returned values should match values gotten when you Search for that courtID in courts
    * For bad input: throw error
    * For non-existing court: throw error


# Data Access Method #7
* Name: editCourt
* **Description**: Stores information on basketball courts, including details like location, amenities, and ratings. Used across: Landing Page, Search Results, Court Details Page, Make a Review Page, Favorites Page
* **Parameters**:
   - `courtID` (int): The unique court identifier is to be updated.
   - Optional fields to update:
       - `courtName` (str)
       - `nets` (0 or 1)
       - `level` (0 or 1)
       - `clean` (0 or 1)
       - `ada` (0 or 1)
       - `inOut` (0 or 1)
       - `hours` (str)
       - `price` (str)
       - `location` (str)
* **Return values**: 
   - `success` (bool): Returns `True` if the update is successful; `False` otherwise.
 * **List of Tests**:

   - **1. Valid Update Test**:
       - **Objective**: Verify that `editCourt` correctly updates specified fields for a valid `courtID`.
       - **Setup**: Ensure the target court entry exists with baseline data.
       - **Test Steps**:
           1. Call `editCourt` with valid values for fields to be updated.
           2. Query the `courts` table using `courtID` to confirm updates.
       - **Expected Outcome**: Only specified fields reflect changes; all other fields remain as before.
       - **Teardown**: Revert the updated fields to baseline data.

   - **2. Invalid Update Test**:
       - **Objective**: Ensure invalid `courtID` or field values return `False` and do not alter the database.
       - **Setup**: Ensure a valid court entry exists.
       - **Test Steps**:
           1. Attempt `editCourt` with an invalid `courtID` (e.g., non-existent ID) and observe the return value.
           2. Attempt `editCourt` with incorrect types (e.g., non-integer for `nets`) or values outside allowed ranges (e.g., `nets=2`).
           3. Query the `courts` table to verify no changes were made.
       - **Expected Outcome**: Returns `False`; no data changes are applied.
       - **Teardown**: No changes to revert as the database state remains unchanged.

   - **3. Partial Update Test**:
       - **Objective**: Confirm that only provided fields are updated, leaving other fields unchanged.
       - **Setup**: Ensure an entry with all fields initialized.
       - **Test Steps**:
           1. Call `editCourt` with only a subset of fields (e.g., `clean=1`, `ada=1`).
           2. Query `courts` using `courtID` to confirm that only specified fields were modified.
       - **Expected Outcome**: Only specified fields reflect changes; all other fields remain unchanged.
       - **Teardown**: Revert updated fields to their original state.
     
# Data Access Method #8
* Name: createUser
* Description: Add a new user to the `users` table.
* Parameters: name(str, the username of the new user), password(str)
* Return values: userID(int, randomized, the userID for the new user)
* List of tests for verifying each access method:
    * Valid strings for a unique name and password should create a new user those entries and a unique userID
    * A name already being used should throw an error
    * Non-string or empty string parameters should throw an error

# Data Access Method #9
* Name: checkUser
* Description: When a user signs in check their name matches the password
* Parameters: name(str), password(str)
* Return values: userID(int)
* List of tests for verifying each access method:
    * Existing user with correct password: Should succeed and sign user in
    * Existing user with incorrect password: Should throw error
    * Non-existing user: Should throw error
    * Invalid parameter types: Should throw error

# Data Access Method #10
* Name: createReview
* Description: User creates a review for a court.
* Parameters: userID (int), courtID (int), comment (str), star(int 1-5)
* Return values: reviewID (int)
* List of tests for verifying each access method:
    * Valid entries for all parameters: should succeed
    * Null, invalid types, empty string in comment, or ints outside range in star: should throw error
    * userID or courtID does not exist: should throw error
    * review for userID and courtID already exists: should replace old review entry

# Data Access Method #11
* Name: getReview
* Description: Get info for a review so it can be displayed. Used to display comments on Court Display page, get all star ratings to calculate avStar, and to show a users reviews
* Parameters: courtID (int)
* Return values:
    * Dictionary with:
        * key: reviewID (int)
        * value: tuple with star value in (0), review comment in (1), and userID in (2)
* List of tests for verifying each access method:
    * Valid courtID should return dictionary with matching reviews
    * Invalid type on non-existing courtID should throw error

# Data Access Method #12
* Name: getPhotos
* Description: Get the photos for a court.
* Parameters: courtID (int)
* Return values:
    * Dictionary with:
        * key: photoID (int)
        * value: photo url
* List of tests for verifying each access method:
    * Valid courtID return dictionary with all matching photos
    * Invalid type on non-existing courtID should throw error

# Data Access Method #13
* Name: getUserReview
* Description: Fetch all reviews for a particular user (to display in Favorites)
* Parameters: userID (int)
* Return values:
    * List of:
        * Dictionary with: 
            * key: reviewID (int)
            * value: tuple with star value in (0), review comment in (1), and userID in (2)
* List of tests for verifying each access method:
    * Valid userID should return list of matching reviews
    * Invalid userID should throw error
    * Valid userID with no reviews should return nothing
