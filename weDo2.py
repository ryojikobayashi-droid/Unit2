minNum = int(input("Enter minimum: "))
maxNum = int(input("Enter maximum: "))
print("Odd numbers from " + str(minNum) + " to " + str(maxNum))
if (minNum % 2) != 1:
    minNum = minNum + 1
for i in range(minNum, maxNum, 2):
    print(i)