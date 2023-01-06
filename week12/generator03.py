def items(list):
    for item in list:
        yield item

list = ("orange", "brown", "blue", "green", "yellow", "pink")
for item in items(list):
    print(item)

