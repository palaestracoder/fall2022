import random

class Dice:
    sides = 6
    def __init__(self):
        self.roll()
    def roll(self):
        self.value = random.randint(1, self.sides)

yahtzee = [Dice(), Dice(), Dice(), Dice(), Dice()]
for die in yahtzee:
    print(f"{die.value}")

