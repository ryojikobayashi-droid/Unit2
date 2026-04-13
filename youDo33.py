text = input("Enter a text: ")
textList = text.split()
print(textList)

countOwl = 0
for i in range(len(textList)):
    if 'owl' in textList[i]
        countOwl = countOwl + 1

print("There are", countOwl, "owls in your text",)