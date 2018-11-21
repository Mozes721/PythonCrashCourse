class User():
    def __init__(self, first_name, last_name, age, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession
        self.login_attempt = 0

    def describe_user(self):
        print("So you are " + self.first_name + ' ' + self.last_name + " and are " + str(self.age) + " " + self.profession + " work with")


    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print("Hello " + full_name)

    def increment_login_attempts(self):
        self.login_attempt += 1

    def reset_login_attempt(self):
        self.login_attempt = 0

user1 = User('Tom', 'Woodhour', 22, 'music developer')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempt)
user1.describe_user()
user1.reset_login_attempt()
print(user1.login_attempt)


