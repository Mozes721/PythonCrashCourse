class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.name + " and cuisine type " + self.cuisine)

    def open_restaurant(self):
        print(self.name + "is open")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine = 'Ice Cream'):
        super().__init__(name, cuisine)
        self.flavours = []

    def show_flavours(self):
        print("\n Displaying flavours: ")
        for ice in self.flavours:
            print(ice + " flavours")

Ice = IceCreamStand('Poncho')

Ice.flavours = ['cream', 'chocolate', 'cherry', 'vannila']
Ice.describe_restaurant()
Ice.show_flavours()