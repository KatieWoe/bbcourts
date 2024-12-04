from flask import Flask, render_template, request
import os
import psycopg2
import db_setup as db
import access_methods as acc


app = Flask(__name__)


def initialize_db():
    """Initialise the database tables and insert initial data."""
    db.delete_tables()
    db.create_tables()
    acc.createCourt(
        "Lakeshore Park Basketball Court",
        4.5,
        1,
        1,
        1,
        1,
        0,
        "10-18",
        "$5.99",
        "Streeterville, Chicago",
        "Nice indoor court",
    )
    acc.createCourt(
        "Douglas Park Outdoor Courts",
        4,
        0,
        1,
        1,
        1,
        1,
        "9-20",
        "$3.99",
        "North Lawndale, Chicago",
        "Most popular among locals",
    )
    acc.createCourt(
        "Margaret Hie Ding Lin Park Basketball Court",
        5,
        1,
        0,
        1,
        0,
        1,
        "11-19",
        "$4.00",
        "Chinatown, Chicago",
        "In a busy corner of Chinatown",
    )
    acc.createCourt(
        "Gill Park Basketball Court",
        3,
        1,
        0,
        1,
        0,
        1,
        "10-19",
        "$7.00",
        "Lakeview East, Chicago",
        "Expensive",
    )


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
    courts = acc.getCourts()
    photos = []
    for court in courts:
        c_photo = acc.getPhotos(court[0])
        if not c_photo:
            photos.append(
                "https://images.unsplash.com/photo-1732564240612-d3f36ec92840?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8YmFza2V0YmFsbCUyMGNvdXJ0fGVufDB8fDJ8fHww"
            )
        else:
            photos.append(c_photo[0][1])
    # return court
    return render_template("listing.html", courts=courts, photos=photos)


@app.route("/courts/<int:court_id>")
def court_details(court_id):
    # Dummy data for the court
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
        "images": [  # Dummy image URLs
            "https://via.placeholder.com/150?text=Image+1",
            "https://via.placeholder.com/150?text=Image+2",
            "https://via.placeholder.com/150?text=Image+3",
        ],
    }

    # Render the template with dummy data
    rendered_html = render_template("court_details.html", court=court)

    # Optionally save the rendered HTML to a static file
    output_path = os.path.join(STATIC_OUTPUT_DIR, f"court_{court_id}.html")
    os.makedirs(STATIC_OUTPUT_DIR, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered_html)

    # Return the rendered template for dynamic viewing
    return rendered_html


@app.route("/reviews/<int:court_id>")
def reviews(court_id):

    court = {"id": court_id, "name": f"Sample Court {court_id}"}

    # Render the review page template
    return render_template("review_page.html", court=court, reviews=reviews)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    initialize_db()
    app.run(debug=True)
