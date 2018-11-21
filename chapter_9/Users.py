class User():
    def __init__(self, first_name, last_name, age, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession

    def describe_user(self):
        print("So you are " + self.first_name + self.last_name + " and are " + str(self.age) + " " + self.profession + " work with")


    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print("Hello " + full_name)


Sam = User("Sam", "Winchester", 36, "Hunter")
Alice = User("Alice", "Weronica", 24, "Barber")
Sam.describe_user()
Alice.describe_user()

Sam.greet_user()
Alice.greet_user()


