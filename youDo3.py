num = int(input("Enter a numer or 0 to ext: "))
while num != 0:
    mul3 = num % 3
    if mul3 == 0:
        print(str(num) + " is a multiple of 3")
    else:
        print(str(num) + " is not a multiple of 3")
    num = int(input("Enter a number or 0 to exit: "))
print("Goodbye")