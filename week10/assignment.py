
quiz = [
    {
        "question": "How many trees are in the forest?",
        "choices": [
            "10",
            "1000",
            "200000",
            "3000000000000"
        ],
        "answer": "3000000000000"
    },
    {
        "question": "What is the oldest type of car?",
        "choices": [
            "London Steam Carriage",
            "Cugnot Fardier",
            "Ford Model T",
            "Daimler-Maybach Stahlradwagen"
        ],
        "answer": "Cugnot Fardier"
    },
    {
        "question": "What color is a carrot?",
        "choices": [
            "Carrot",
            "Purple",
            "Green",
            "Yellow",
            "Pumpkin",
            "Black"
        ],
        "answer": "Carrot"
    }
]

problemNumber = 0
correct = 0
for problem in quiz:
    problemNumber += 1
    print(f"Question {problemNumber}: {problem['question']}")

    for choice in problem['choices']:
        print(f"  {choice}")

    guess = input("Your guess: ")
    if guess == problem['answer']:
        correct += 1
        print(f"You are correct!")
    else:
        print(f"Incorrect.")

    print()  # print a blank line for space

print(f"Correct: {correct} of {problemNumber} ({correct * 100 / problemNumber}%)")







