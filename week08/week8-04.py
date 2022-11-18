import os

sourceFile = __file__
sourceDir = os.path.dirname(__file__)
newPath = os.path.join(sourceDir, 'my-file.txt')

print(f"sourceFile: {sourceFile}")
print(f"sourceDir: {sourceDir}")
print(f"newPath: {newPath}")


