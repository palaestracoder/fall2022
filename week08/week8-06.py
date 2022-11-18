import os

sourceDir = os.path.dirname(__file__)

name = input("What is your name? ")

f = open(os.path.join(sourceDir, "week8-05-output.txt"), "w")
f.write(f"Hello, {name}!")
f.close()

