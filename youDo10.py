import random
rounds = int(input("Enter number of rounds: "))
for i in range(1, rounds + 1):
    fullText = ""
    for rounds in range(1, rounds + 1):
        text = str(random.randint(1, 10))
        fullText = text + " " + fullText
    print("Round ", str(i) + "...", fullText)