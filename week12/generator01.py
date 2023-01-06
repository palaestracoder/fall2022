def petGenerator():
    yield "Fluffy"
    yield "Rex"
    yield "Squeeky"

for pet in petGenerator():
    print(pet)


    