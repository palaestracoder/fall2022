import random

class Dice:
    sides = 6
    def __init__(self):
        self.roll()
    def roll(self):
        self.value = random.randint(1, self.sides)

die = Dice()
die.sides = 3
die.roll()
print(f"{die.value}")

