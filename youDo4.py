password = input("Enter password: ")
control = 0
while control != 2:
    if password == "password":
        print("Welcome!")
        control = 2
    else:
        print("Error!")
        control = control + 1
        password = input("Enter password: ")