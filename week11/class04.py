import random

class Dice:
    def roll(self):
        self.value = random.randint(1, 6)

yahtzee = [Dice(), Dice(), Dice(), Dice(), Dice()]
#for die in yahtzee:
#    die.roll()

for die in yahtzee:
    print(f"{die.value}")

