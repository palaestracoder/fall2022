import random

class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.roll()
    def roll(self):
        self.value = random.randint(1, self.sides)

die = Dice(8)
print(f"{die.value}")

