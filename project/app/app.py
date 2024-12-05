from flask import Flask, render_template, request
import os
import psycopg2
import db_setup as db
import access_methods as acc



app = Flask(__name__)


# def initialize_db():
#     """Initializes the database by deleting and recreating tables, then seeding data."""
#     print("Initializing database...")

#     # Delete existing tables
#     print("Deleting existing tables...")
#     db.delete_tables()  # Assuming this function drops all the tables in your database

#     # Create fresh tables
#     print("Creating new tables...")
#     db.create_tables()  # Assuming this function creates all required tables

#     # Seed users
#     print("Seeding users...")
#     generate_dummy_users(4)  # Creates 4 dummy users

#     # Seed courts and reviews
#     print("Seeding courts and reviews...")
#     generate_dummy_courts_with_reviews(court_count=20, max_reviews_per_court=10)  # 20 courts with up to 10 reviews each

#     print("Database initialization complete!")


def initialize_db():
    """Initializes the database by ensuring tables exist, without reseeding."""
    print("Initializing database...")

    # Ensure tables exist without modifying existing data
    try:
        db.create_tables()  # Creates tables if they don't already exist
        print("Database tables checked and ready.")
    except Exception as e:
        print(f"Error initializing database: {e}")

    print("Database initialization complete.")


################################################################

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
    courts = acc.getCourts()  # Example: [(id, name, avStar, ..., location, description), ...]

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
            photos.append("https://unsplash.com/photos/a-hand-holding-a-basketball-up-to-a-ball-bRjQF25-C_o")

    return render_template("listing.html", courts=courts, photos=photos)




@app.route("/courts/<int:court_id>")
def court_details(court_id):
    court = {
        "id": court_id,
        "name": f"Sample Court {court_id}",
        "location": f"{court_id} Court Avenue, Basketball City",
        "amenities": [
            "Basketball Hoop",
            "Benches",
            "Lights",
            "Restroom",
            "Parking Lot",
        ],
        "rating": 4.5,
        "description": f"Sample Court {court_id} is an excellent place for basketball enthusiasts, featuring premium hoops and well-maintained facilities.",
        "images": [
            "https://via.placeholder.com/150?text=Image+1",
            "https://via.placeholder.com/150?text=Image+2",
            "https://via.placeholder.com/150?text=Image+3",
        ],
    }

    rendered_html = render_template("court_details.html", court=court)

    output_path = os.path.join(STATIC_OUTPUT_DIR, f"court_{court_id}.html")
    os.makedirs(STATIC_OUTPUT_DIR, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered_html)

    return rendered_html

@app.route("/reviews/<int:court_id>")
def reviews(court_id):
    court = {"id": court_id, "name": f"Sample Court {court_id}"}
    return render_template("review_page.html", court=court, reviews=reviews)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    initialize_db()  # Automatically reinitialize the database
    app.run(debug=True)
