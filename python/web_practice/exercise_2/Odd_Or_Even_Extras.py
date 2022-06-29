integer = int(float(input("Enter an integer here:")))
divided = integer % 2
if integer % 4 == 0:
    print(integer, "is even and divisible by 4")
elif divided == 1:
    print(integer, "is odd")
else:
    print(integer, "is even, but not divisible by 4")
num = int(float(input("Enter another integer here:")))
check = int(float(input("Enter an integer to divide it by here:")))
ans = num % check
if ans == 0:
    print(num, "is evenly divisible by", check)
else:
    print(num, "is NOT evenly divisble by", check)