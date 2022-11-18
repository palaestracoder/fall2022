names = ("dogs", "cats")
numbers = []
for name in names:
    numbers.append(float(input(f"How many {name}? ")))

print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")

