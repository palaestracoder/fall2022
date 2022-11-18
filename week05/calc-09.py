scale = 5
def grow(x):
    return x * scale
def shrink(x):
    return x / scale
number = 123
print("scale is", scale)
print(grow(number), shrink(number))
