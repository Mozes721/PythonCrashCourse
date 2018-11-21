class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.name + " and cuisine type " + self.cuisine)

    def open_restaurant(self):
        print(self.name + "is open")

    def close_restaurant(self):
        return 'Closed'

restaurant = Restaurant("Shark tank ", "Mediterranean")
restaurant2 = Restaurant("Golden Goose", 'Nordic')
restaurant3 = Restaurant("Mehico Calibra", "Mexican")
print(restaurant.name, restaurant.cuisine)

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant.open_restaurant()
