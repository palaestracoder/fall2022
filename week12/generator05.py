def items(list, prefix, mid):
    for item in list:
        if item.startswith(prefix) or mid in item:
            yield item

list = ("orange", "brown", "blue", "green", "yellow", "pink")
for item in items(list, "o", "n"):
    print(item)

