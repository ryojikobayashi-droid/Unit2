numList = []
for i in range(6):
    numList.append(int(input("Enter a number: ")))
print(numList)
biggest_int = numList[0]
for i in range(1,len(numList)):
    if numList[i] > biggest_int:
        biggest_int = numList[i]
print("biggest inst is now", biggest_int)