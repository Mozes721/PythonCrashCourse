class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " sitting")

    def roll(self):
        print(self.name.title() + "rolling")



dog = Dog('Amir',14)
dog.sit()