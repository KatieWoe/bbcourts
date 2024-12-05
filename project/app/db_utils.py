import random
import access_methods as acc  # Your data access functions

def generate_dummy_courts_with_reviews(court_count, max_reviews_per_court=10):
    """Generates and seeds dummy court data with random reviews into the database."""
    locations = ["Chicago", "Los Angeles", "New York", "Phoenix", "Austin"]
    descriptions = [
        "Beautiful outdoor court.",
        "Spacious indoor facility.",
        "Popular community court.",
        "Well-maintained park.",
        "Scenic court with amazing views."
    ]

    for i in range(court_count):
        # Generate a random court
        court = {
            "courtName": f"Random Court {i+1}",
            "nets": random.choice([0, 1]),
            "level": random.choice([0, 1]),
            "clean": random.choice([0, 1]),
            "ada": random.choice([0, 1]),
            "inOut": random.choice([0, 1]),
            "hours": f"{random.randint(6, 12)} AM - {random.randint(6, 11)} PM",
            "price": random.choice(["Free", "$3", "$5", "$10"]),
            "location": f"{random.choice(locations)}, USA",
            "description": random.choice(descriptions)
        }

        # Insert the court and get its ID
        try:
            court_id = acc.createCourt(
                court["courtName"],
                None,  # avStar will be calculated after reviews
                court["nets"],
                court["level"],
                court["clean"],
                court["ada"],
                court["inOut"],
                court["hours"],
                court["price"],
                court["location"],
                court["description"],
            )
            print(f"Successfully created court: {court['courtName']} (ID: {court_id})")

            # Generate random reviews for the court
            review_count = random.randint(1, max_reviews_per_court)
            for j in range(review_count):
                try:
                    review = acc.createReview(
                        userID=random.randint(1, 4),  # User IDs from 1 to 100 (matches the number of seeded users)
                        courtID=court_id,
                        star=random.randint(1, 5),  # Random star rating between 1 and 5
                        comment="Random review comment"  # Placeholder comment
                    )
                    print(f"  - Created review #{j+1} for court {court['courtName']}")
                except Exception as review_error:
                    print(f"  - Error creating review for court {court['courtName']}: {review_error}")

            # Calculate the average star rating after generating reviews
            avStar = acc.calcAvStar(court_id)

            # Update the court's average star rating
            try:
                acc.editCourt(
                    courtID_edit=court_id,
                    courtName=court["courtName"],
                    avStar=avStar,
                    nets=court["nets"],
                    level=court["level"],
                    clean=court["clean"],
                    ada=court["ada"],
                    inOut=court["inOut"],
                    hours=court["hours"],
                    price=court["price"],
                    location=court["location"],
                    description=court["description"],
                )
                print(f"  - Updated court {court['courtName']} with average star rating: {avStar}")
            except Exception as edit_error:
                print(f"  - Error updating court {court['courtName']}: {edit_error}")

        except Exception as court_error:
            print(f"Error creating court: {court_error}")


def generate_dummy_users(count):
    """Generates and seeds dummy users into the database."""
    for i in range(count):
        try:
            user = acc.createUser(
                name=f"User{i+1}",
                password="password123"  # Placeholder password
            )
            print(f"Successfully created user: User{i+1}")
        except Exception as user_error:
            print(f"Error creating user: {user_error}")

