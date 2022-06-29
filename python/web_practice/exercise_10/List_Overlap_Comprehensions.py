import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for d in a:
    if d in b and d not in c:
        c.append(d)
print(c)

# Random List Comparison
testvar =  input("Enter for Random List Comparison")
new_1 = []
rand_1 = random.sample(range(1,100), random.randint(1,30))
rand_2 = random.sample(range(1,100), random.randint(1,30))
print("First random list:", rand_1)
print("Second random list:", rand_2)
for digit in rand_1:
    if digit in rand_2 and digit not in new_1:
        new_1.append(digit)
print("Integers in common:", new_1)