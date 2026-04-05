def replace_at_index(word):
    index = int(input("Enter an index: "))
    print("New word: " + word[0:index] + "-" + word[index+1:])
replace_at_index(input("Enter a word: "))