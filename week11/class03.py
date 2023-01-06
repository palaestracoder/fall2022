import random

class Dice:
    def roll(self):
        self.value = random.randint(1, 6)

d = Dice()
d.roll()
print(f"{d.value}")

