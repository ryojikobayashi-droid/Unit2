def replace_at_index(word):
    index = int(input("Enter an index: "))
    replace = input("Enter a word to replace: ")
    print("New word: " + word[0:index] + replace + word[index+1:])
replace_at_index(input("Enter a word: "))