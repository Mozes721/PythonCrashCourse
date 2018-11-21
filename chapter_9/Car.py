class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You cant turn back")
    def increment_odometer(self,milage):
        self.odometer_reading += milage
class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " kwv battery.")

    def get_range(self):

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 90:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles full charge"
        print(message)


class ElectricCar(Car,Battery):
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery_size = Battery()



my_test = ElectricCar('tesla', 'model s', '2016')
print(my_test.get_descriptive_name())
my_test.battery_size.describe_battery()
my_test.battery_size.get_range()


