class Restaurant():

    def __init__(self, name, cuisine):
        self.name = name.title()
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print("\nThe name of the restaurant is " + self.name + " and cuisine type " + self.cuisine)

    def open_restaurant(self):
        msg = self.name + "is open come in!"
        print("\n" + msg)

    def set_numbers_served(self, numbers_served):
        self.numbers_served = numbers_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()


print("\nNumber served: " + str(restaurant.numbers_served))
restaurant.increment_number_served(50)
print("\nNumber served: " + str(restaurant.number_served))

restaurant1 = Restaurant('Galeo', 'Mexican')
restaurant1.open_restaurant()
restaurant1.numbers_served = 50
print(str(restaurant1.numbers_served))

set = str(restaurant.set_numbers_served(3))