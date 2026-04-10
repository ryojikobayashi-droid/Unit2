names = ["Omar", "Ronan", "Trent", "Zohair"]
gpaScore = []
gpaScore.append(4.3)
gpaScore.append(2.3)
gpaScore.append(1)
gpaScore.append(3.4)

print(names)
print(gpaScore)

names.insert(1,"Isacc")
gpaScore.insert(1, 4.1)

names.pop(3)
gpaScore.pop(3)

print(names)
print(gpaScore)

ind = 0
for value in gpaScore:
    if value == 3:
        gpaScore.pop(ind)
        names.pop(ind)
    ind = ind + 1