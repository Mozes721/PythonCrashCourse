from chapter_9.Battery_Upgrade import Car, Battery, ElectricCar


my_test = ElectricCar('tesla', 'model s', '2016')
my_test.battery_size.describe_battery()
my_test.battery_size.upgrade_battery()
my_test2 = Car('BMW', 'R-17', '2017')
my_test2.update_odometer(20)

