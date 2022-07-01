from datetime import datetime

name = input("Enter Name Here: ")
age = int(float(input("Enter Current Age Here: ")))
year = (datetime.now().year - age) + 100
print(2 * (name, ", you will be 100 years old in the year", year))