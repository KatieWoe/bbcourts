# This file holds the classes describing the entities for the bbcourts website

# The Court class holds the features the a post about a court should have
class Court:
    #name of the court
    name_of_court = ""
    def set_name(self, name):
        self.name_of_court = name
        
    #identifying number of court
    court_id = 0
    def set_id(self, new_id):
        self.court_id = new_id
    
    #array of all the ratings given to the court
    rating_array = []
    def add_rating(self, rating):
        self.rating_array.append(rating)
    
    #average of the rating array
    average_rating = None
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

#The Comment class holds the features a comment on a post should have
class Comment:
    #id of court comment is on
    court_id = 0
    def set_court(self, court):
        self.court_id = court
    
    #id of comment
    comment_id = 0
    def set_comment_id(self, c_id):
        self.comment_id = c_id
    
    #id of parent comment
    parent_id = None
    def set_parent(self, parent):
        self.parent_id = parent
    
    #time comment was mad
    comment_time = 0
    def set_time(self, t):
        self.comment_time = t
    
    #connent of comment
    comment = ""
    def set_comment(self, comment):
        self.comment = comment