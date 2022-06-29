def num():
    return int(input("Enter how long the Fibonacci sequence should be:"))

x = num()
y = 1
digit_1 = 0
digit_2 = 1
z = 1
fibo = [1]
while z < x:
    fibo.append(y)
    y = fibo[digit_1] + fibo[digit_2]
    z = z + 1
    digit_1 = digit_1 + 1
    digit_2 = digit_2 + 1
print(fibo)