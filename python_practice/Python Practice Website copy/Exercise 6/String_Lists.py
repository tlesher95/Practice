# Check for Palindrome 
try:
    word = input("Enter Word:")
    x = int(0)
    y = int(0)
    # To find length of word
    for letter in word:
        y = y + 1
        print(y)
    while y > 0:
        if word[x] == word[y]:
            x = x + 1
            y = y - 1
            print("True")
        else:
            print("False")
except:
    word = input("Enter a word:")
    if word == word[::-1]:
        print("Yes, it's a palindrome!")
    else:
        print("No, not a palindrome :(")
