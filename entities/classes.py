# This file holds the classes describing the entities for the bbcourts website

# The Court class holds the features the a post about a court should have
class Court:
    #name of the court
    name_of_court = ""
    def set_name(self, name):
        self.name_of_court = name
    
    #array of all the ratings given to the court
    rating_array = []
    def add_rating(self, rating):
        self.rating_array.append(rating)
    
    #average of the rating array
    average_rating = float("nan")
    def calc_av(self):
        if len(self.rating_array) > 0:
            self.average_rating = sum(self.rating_array) / len(self.rating_array)
        else:
            self.average_rating = float("nan")
    
    #description of the court quality
    quality = ""
    def set__quality(self, quality):
        self.quality = quality
    
    #is the court accessible?
    ada_accessible = False
    def set_ada(self, ada):
        self.ada_accessible = ada
    
    #cost to get in
    admit_price = 0
    def set_price(self, price):
        self.admit__price = price
    
    #indoor or outdoor
    in_or_out = ""
    def set_in_out(self, inout):
        self.in_or_out = inout
    
    #location
    location = ""
    def set_location(self, locate):
        self.location = locate
    
    #Picture of court
    pic_of_court = ""
    def set_pic(self, pic):
        self.pic_of_court = pic