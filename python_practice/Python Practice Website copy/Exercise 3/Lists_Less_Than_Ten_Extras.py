a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for digit in a:
    if digit < 5:
        b.append(digit)
print(b)

c = int(input("Enter an integer:"))
d = []
for digit in a:
    if digit < c:
        d.append(digit)
print(d)