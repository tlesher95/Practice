#Ask for user input of a sentence or series of strings, print them in reverse order

#Method 1
def reverse_1(x):
    y = x.split()
    result = []
    for word in y:
        result.insert(0,word)
    return " ".join(result)


#Method 2
def reverse_2(x):
    y = x.split()
    return " ".join(y[::-1])


#Method 3
def reverse_3(x):
    y=x.split()
    return " ".join(reversed(y))


#Method 4
def reverse_4(x):
    y = x.split()
    y.reverse()
    return " ".join(y)


#Test
test1 = input("Enter a sentence: ")
print(reverse_1(test1))
print(reverse_2(test1))
print(reverse_3(test1))
print(reverse_4(test1))