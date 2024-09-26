# This file holds the classes describing the entities for the bbcourts website

# The Court class holds the features the a post about a court should have
class Court:
    #name of the court
    name_of_court = ""
    
    #array of all the ratings given to the court
    rating_array = []
    
    #average of the rating array
    average_rating = float("nan")
    
    #description of the court quality
    quality = ""
    
    #is the court accessible?
    ada_accessible = False
    
    #cost to get in
    admit_price = 0
    
    #indoor or outdoor
    in_or_out = ""
    
    #location
    location = ""
    
    #Picture of court
    pic_of_court = ""