# Check Odd or Even
integer = int(float(input("Enter an integer here:")))
divided = integer % 2
if divided == 1:
    print(integer, "is odd")
else:
    print(integer, "is even")