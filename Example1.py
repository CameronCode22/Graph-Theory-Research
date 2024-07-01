class Person:
    #attributes
    def __init__(self, age, weight, height, first_name, last_name, catch_phrase):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase = catch_phrase
    #methods
    def walk(self):
        print("walking...")
    def run(self):
        print("Running...")

class Bottle:
    def __init__(self, volume, type_):
        self.volume = volume
        self.type_ = type_

    def pour(self):
        print("Pouring...")
    def fill(self):
        print("Filling...")
    def recycle(self):
        print("Recycling")

#establishing a user
user = Person(25, 80, 177, "John","Snow","You know nothing, Jon Snow")
#using the method
#user.walk()

bottle = Bottle(100, "Big")

print(bottle.type_)

#print(user)