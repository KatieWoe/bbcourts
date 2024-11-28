from flask import Flask, render_template
import os


app = Flask(__name__)

# Directory to save static files
STATIC_OUTPUT_DIR = "static_site"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/listing')
def listing():
    return render_template('listing.html')

@app.route('/courts/<int:court_id>')
def court_details(court_id):
    # Dummy data for the court
    court = {
        "id": court_id,
        "name": f"Sample Court {court_id}",
        "location": f"{court_id} Court Avenue, Basketball City",
        "amenities": ["Basketball Hoop", "Benches", "Lights", "Restroom", "Parking Lot"],
        "rating": 4.5,
        "description": f"Sample Court {court_id} is an excellent place for basketball enthusiasts, featuring premium hoops and well-maintained facilities.",
        "images": [  # Dummy image URLs
            "https://via.placeholder.com/150?text=Image+1",
            "https://via.placeholder.com/150?text=Image+2",
            "https://via.placeholder.com/150?text=Image+3"
        ]
    }

    # Render the template with dummy data
    rendered_html = render_template('court_details.html', court=court)

    # Optionally save the rendered HTML to a static file
    output_path = os.path.join(STATIC_OUTPUT_DIR, f"court_{court_id}.html")
    os.makedirs(STATIC_OUTPUT_DIR, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered_html)

    # Return the rendered template for dynamic viewing
    return rendered_html

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.run(debug=True)