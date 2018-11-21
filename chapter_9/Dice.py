from random import randint

class Die():
    def __init__(self,sides=6):
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)

d6 = Die()

results = []

for i in range(10):
    result = d6.roll_dice()
    results.append(result)
print("Rolled 10 times!")
print(results)

d10 = Die(sides=10)

for i in range(10):
    result = d10.roll_dice()
    results.append(result)
print("Rolled 10 times!")
print(results)
