nam = input("Enter Name Here:")
nam = nam.capitalize()
age = int(input("Enter Current Age Here:"))
num = int(input('Enter # of Times to Repeat Message:'))
century = str((2022 - age) + 100)
print(num * (f"{nam}, you will be 100 years old in the year: {century}"))