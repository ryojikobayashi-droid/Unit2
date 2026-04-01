import random
minLim = int(input("Enter a minimum: "))
maxLim = int(input("Enter a maximum: "))
ans = ""
while ans != "No":
    print("Generating a random number...")
    print("")
    num = random.randint(minLim, maxLim)
    if (num % 2) == 1:
        modulus = "ODD"
    else:
        modulus = "EVEN"
    if num > 50:
        size = "BIG"
    else:
        size = "SMALL"
    half = (maxLim + minLim) / 2
    if num > half:
        over = "above half yor range"
    else:
        over = "below half your range"
    print("Your number is " + str(num))
    print("Your number is " + modulus)
    print("Your number is " + size)
    print("Your number is " + over)
    ans = input("Would you like to try again? ")
print("Goodbye")