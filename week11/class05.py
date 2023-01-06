import random

class Dice:
    def __init__(self):
        self.roll()
    def roll(self):
        self.value = random.randint(1, 6)

yahtzee = [Dice(), Dice(), Dice(), Dice(), Dice()]
for die in yahtzee:
    print(f"{die.value}")

