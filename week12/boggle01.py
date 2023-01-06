import random

dice = (
    ("R", "I", "F", "O", "B", "X"),
    ("I", "F", "E", "H", "E", "Y"),
    ("D", "E", "N", "O", "U", "S"),
    ("U", "T", "O", "K", "N", "D"),
    ("H", "M", "S", "R", "A", "O"),
    ("L", "U", "P", "E", "T", "S"),
    ("A", "C", "I", "T", "O", "A"),
    ("Y", "L", "G", "K", "U", "E"),
    ("Qu", "B", "M", "J", "O", "A"),
    ("E", "H", "I", "S", "P", "N"),
    ("V", "E", "T", "I", "G", "N"),
    ("B", "A", "L", "I", "Y", "T"),
    ("E", "Z", "A", "V", "N", "D"),
    ("R", "A", "L", "E", "S", "C"),
    ("U", "W", "I", "L", "R", "G"),
    ("P", "A", "C", "E", "M", "D")
)

def rollDice():
    roll = list(dice)
    random.shuffle(roll)
    for die in roll:
        yield random.choice(die)

board = []
roll = rollDice()
for row in range(0,4):
    newRow = []
    for col in range(0, 4):
        newRow.append(next(roll))
    board.append(newRow)

print(board)

