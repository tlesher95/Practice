x = int(input("Enter and Integer for its Divisors:"))
y = []
for digits in list(range(1, x + 1)):
    if x % digits == 0:
        y.append(digits)
print(y)

