a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for digit in a:
    if digit in b:
        c.append(digit)
print(c)

import random
randlist1 = random.sample(range(1,100), 26)
randlist2 = random.sample(range(1,100), 17)
print(randlist1)
print(randlist2)
finlist = []
for num in randlist1:
    if num in randlist2:
        finlist.append(num)
print(finlist)
