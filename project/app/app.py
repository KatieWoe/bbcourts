from flask import Flask, render_template, request
import os
import psycopg2
import db_setup as db
import access_methods as acc

import sys
import traceback

app = Flask(__name__)


# Directory to save static files
STATIC_OUTPUT_DIR = "static_site"



def calcAvStar(courtID_calc):
    """
    Get the star rating from reviews for the court given. Calculate the average and return the average.
    """
    try:
        connection = psycopg2.connect(db.DATABASE_URL)
        cursor = connection.cursor()

        cursor.execute(
            """
        SELECT star FROM reviews WHERE courtID = %s;
        """,
            (courtID_calc,),
        )

        stars_tup = cursor.fetchall()
        stars = []
        for row in stars_tup:
            stars.append(row[0])
        
        # Handle case where there are no reviews
        if not stars:
            return 0
            
        avStar = sum(stars) / len(stars)

        connection.close()
        return avStar

    except Exception as e:
        print(f"Error calculating average star rating: {str(e)}")
        return 0
    finally:
        if 'connection' in locals():
            connection.close()


@app.errorhandler(Exception)
def handle_error(e):
    print(traceback.format_exc(), file=sys.stderr)
    return str(e), 500


@app.route("/")
def index():
    return render_template("index.html", include_header_footer=True)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login")
def login():
    return render_template("login.html", include_header_footer=False)


@app.route("/listing")
def listing():
    # Fetch all courts from the database
    courts = (
        acc.getCourts()
    )  # Example: [(id, name, avStar, ..., location, description), ...]

    # Replace None avStar values with 0
    courts = [
        tuple(0 if (val is None and idx == 2) else val for idx, val in enumerate(court))
        for court in courts
    ]

    # Fetch associated photos for courts
    photos = []
    for court in courts:
        court_photos = acc.getPhotos(court[0])  # Assuming `court[0]` is the court ID
        if court_photos:
            photos.append(court_photos[0][1])  # Use the first photo URL
        else:
            photos.append(
                "https://unsplash.com/photos/a-hand-holding-a-basketball-up-to-a-ball-bRjQF25-C_o"
            )

    return render_template("listing.html", courts=courts, photos=photos)



@app.route("/courts/<int:court_id>")
def court_details(court_id):
    try:
        # Fetch court details
        court = acc.getCourt(court_id)
        if not court:
            return render_template("404.html"), 404
        
        # Fetch photos
        photos = acc.getPhotos(court_id)
        
        # Fetch and process reviews
        reviews_dict = acc.getReviews(court_id)
        if not reviews_dict:
            reviews = []
            total_reviews = 0
            rating = 0
        else:
            reviews = [
                {
                    'id': review_id,
                    'username': review_data[0],
                    'rating': float(review_data[1]),
                    'image': review_data[2] or 'https://via.placeholder.com/150',
                    'text': review_data[3]
                }
                for review_id, review_data in reviews_dict.items()
            ]
            total_reviews = len(reviews)
            rating = calcAvStar(court_id)

        # Calculate star display values
        full_stars = int(rating)
        partial_star = 1 if (rating - full_stars) >= 0.5 else 0
        empty_stars = 5 - full_stars - partial_star

        # Debugging
        if os.getenv("FLASK_ENV") == "development":
            print("Debug - First review:", reviews[0] if reviews else "No reviews")
            print("Debug - Average rating:", rating)

        # Render template
        return render_template(
            "court_details.html",
            court=court,
            photos=photos,
            reviews=reviews,
            total_reviews=total_reviews,
            full_stars=full_stars,
            partial_star=partial_star,
            empty_stars=empty_stars,
            int=int
        )
    except Exception as e:
        print("Error occurred:")
        print(traceback.format_exc())
        return f"An error occurred: {str(e)}", 500


@app.route("/reviews/<int:court_id>")
def reviews(court_id):
    court = {"id": court_id, "name": f"Sample Court {court_id}"}
    return render_template("review_page.html", court=court, reviews=reviews)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.debug = True  # Enable debug mode
    app.run()