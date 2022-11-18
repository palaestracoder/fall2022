names = ("dogs", "cats")
numbers = []
for names in names:
    countText = input(f"How many {name}?")
    count = float(countText)
    numbers.append(count)

print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
