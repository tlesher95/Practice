x = input("Enter Name:")
x = x.capitalize()
w = float(input("Enter Military Time HHMM:"))
if w <= 1159:
    r = "Good Morning"
elif w >= 1200 and w <= 1759:
    r = "Good Afternoon"
elif w >= 1800 and w <=2359:
    r = "Good Evening"
else:
    print("Invalid Input")
print(r , x)
