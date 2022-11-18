import os

sourceDir = os.path.dirname(__file__)

f = open(os.path.join(sourceDir, "week8-02-input.txt"))
name = f.readline()
print(f"Hello, {name}!")
f.close()

