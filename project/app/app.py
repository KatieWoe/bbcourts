from flask import Flask, render_template, request
import os
import psycopg2
import db_setup as db
import access_methods as acc

app = Flask(__name__)

# Directory to save static files
STATIC_OUTPUT_DIR = "static_site"


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
    court = acc.getCourt(court_id)  # Get court details
    if not court:
        return render_template("404.html"), 404

    # Preprocess rating logic in Python
    rating = court[2] or 0
    full_stars = int(rating)  # Full stars
    partial_star = 1 if (rating - full_stars) >= 0.5 else 0
    empty_stars = 5 - full_stars - partial_star

    photos = acc.getPhotos(court_id)  # Get photos for the court
    reviews = acc.getReviews(court_id)  # Get reviews for the court

    return render_template(
        "court_details.html",
        court=court,
        photos=photos,
        reviews=reviews,
        full_stars=full_stars,
        partial_star=partial_star,
        empty_stars=empty_stars,
    )




@app.route("/reviews/<int:court_id>")
def reviews(court_id):
    court = {"id": court_id, "name": f"Sample Court {court_id}"}
    return render_template("review_page.html", court=court, reviews=reviews)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
