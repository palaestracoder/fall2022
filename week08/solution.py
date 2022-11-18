import os

sourceDir = os.path.dirname(__file__)
filePath = os.path.join(sourceDir, "assignment.txt")
f = open(filePath, encoding="utf8")

count = 0
for line in f.readlines():
    words = line.split(" ")
    count = count + len(words)

print(f"Words: {count}")
f.close()