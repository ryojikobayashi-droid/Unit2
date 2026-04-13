text = input("Enter text: ")
list1 = list(text)
print(list1)
for i in list1:
    if i == "i":
        i = "!"
print(list1)