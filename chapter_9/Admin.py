class User():
    def __init__(self, first_name, last_name, age, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession

    def describe_user(self):
        print("So you are " + self.first_name + ' '+ self.last_name + " and are " + str(self.age) + " " + self.profession + " work with")


    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print("Hello " + full_name)

class Admin(User):
    def __init__(self,first_name, last_name, age, profession):
        super().__init__(first_name,last_name, age, profession)
        self.privileges = Privileges()


class Privileges():
    def __init__(self, privileges = []):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges: ")
        if self.privileges:
            for privilege in self.privileges:
                print('-- ' + privilege)
        else:
            print("- This user has no privileges.")




adm = Admin('Richard', 'Taujenis', 25, 'analist')
adm.describe_user()
print("\nAdding privileges...")
adm_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
adm.privileges.privileges = adm_privileges
adm.privileges.show_privileges()