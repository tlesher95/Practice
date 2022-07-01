from datetime import datetime

name = input("Enter Name Here: ").title()
age = int(input("Enter Current Age Here: "))
num = int(input('Enter # of Times to Repeat Message: '))
year = str((datetime.now().year - age) + 100)
print(num * (f"{name.strip()}, you will be 100 years old in the year {year}\n"))