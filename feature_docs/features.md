Wire Frames: https://miro.com/app/board/uXjVLZRMTL4=/

Pages: Main Landing, Search Results/Court Listings, Court Details, Make a Review/Raiting, Favorites Page

Features

Main Landing Page: (Toanp)

Court:
* URL Route: /<court_id>/
* Links To:
    Review Form
    Search Page through search bar
    Outside link to google maps and weather
* Name of Court
* Court ID
    Unique ID for each court
    Generated upon entry creation.
    Allows courts to have similar/same names (such as YMCA)
    Allows info to be retained when changes are made, such as new court name
    Can be used to associate with other features, such as comments and photo gallery
* Average Rating
    5 Star System
    Users can enter a star rating
    Average of all user submitted ratings is displayed
* Court Quality 
    Series of features and yes no or good average bad
    Determined by user vote?
        * Nets Present
        * Level Court/No Cracks
        * Clean
        * ADA Accessible
        * Equipment Available
* In/Out Doors
* Hours of Operation
    May take several lines if it varies by day
    7 lines max
* Pricing Info
    Marked with the price(s) or as Free
* Location
    Address
    Connect to Google Maps
* Current Weather
    Use Address to pull weather data in the area
* Photo Gallery
* Comment Section

Make Review: (Jonathan):
* URL Route: /<court_id>/reviews/
* Links to:
    * Court Page
    * Other Courts on the site
    * Search Bar
* Search Bar:
    * Include an input field for users to search reviews by name, keywords, or rating.
    * Placeholder text: "Search Reviews"

* Average Rating (5-Star System)
    * Display a star-based system (average of all user ratings).
    * Add text: "Average Rating: X/5" where "X" is dynamically calculated based on all user ratings.

* Individual Reviews:
    * Reviewer’s Username
    * Rating: x/5 stars visual 
    * Date: When the review was submitted.
    * Review Text: User's feedback.

* Other Courts Section:
    * Thumbnail of the court 
    * Name of the court
    * Average rating out of 5 stars
    * Link to the specific court’s page for more information.
  
Search Results:
* URL Route: /search?search_entry
* Links to:
    Court Pages from results
    Search Results from search bar
* Search looks for matches in:
    Name
    Address
* Sort by:
    Rating
    Alphabetic
    Price
* Results Show:
    First Gallery Image
    Name of Court
    Average Rating
    Address
    In/Out Door
    Price

Favorites: (Jaekyeong Lee)
