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

class coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

class wordFinder:
    def __init__(self, board, coords):
        self.board = board
        self.visited = [coords]                                 # track the coordinates for each letter
        self.wordLetters = [self.board[coords.row][coords.col]] # a list for each letter of the found word

    def move(self, direction):
        # move in the requested direction
        current = self.visited[-1]   # start with where we've visited last
        next = coordinate(current.row, current.col)
        if "up" in direction:
            next.row -= 1
        if "down" in direction:
            next.row += 1
        if "left" in direction:
            next.col -= 1
        if "right" in direction:
            next.col += 1

        # check if the new position is valid, and return False if it is not
        if next.row < 0 or next.col < 0 or next.row > 3 or next.col > 3:
            return False  # off the board
        if next in self.visited:
            return False  # already visited

        # the new position is good, move to it and return True
        self.visited.append(next)
        letter = self.board[next.row][next.col]
        self.wordLetters.append(letter)
        return True

    def moveBack(self):
        # remove the last visited coordinate and its corresponding letter
        del self.visited[-1]
        del self.wordLetters[-1]

    def possibleWords(self):
        for direction in ("up", "down", "left", "right", "up-left", "up-right", "down-left", "down-right"):
            if self.move(direction):
                # we just moved to a potential word; emit it
                if len(self.wordLetters) >= 3:
                    word = "".join(self.wordLetters)
                    yield word

                # try moving again in all possible directions, and emit each word
                for subword in self.possibleWords():
                    yield subword

                # possibilities in this direction are exhausted, move back and try another direction
                self.moveBack()

def allWords(board):
    for row in range(0, 4):
        for col in range(0, 4):
            finder = wordFinder(board, coordinate(row, col))
            for word in finder.possibleWords():
                yield word

count = 0
for word in allWords(board):
    count += 1
    if count % 100000 == 0:
        print(count)



            

    

    