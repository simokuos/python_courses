# by Simo Kuosmanen

# 1. User gives a value and our program tells if the value is > 100 or not

integer_one = int(input("Value:"))
if(integer_one > 100):
    print(integer_one, " is larger than 100")
else:
    print(integer_one, " is smaller than 100")

# 2. User enters a weekday number and the program tells the name of the day

weekday_number = int(input("weekday by number:"))

if(weekday_number == 1):

    print("monday")

elif(weekday_number == 2):

    print("tuesday")

elif(weekday_number == 3):

    print("wednesday")
elif(weekday_number == 4):

    print("thursday")

elif(weekday_number == 5):

    print("friday")

elif(weekday_number == 6):

    print("saturday")

elif(weekday_number == 7):

    print("sunday")

# 3. Program calculates BMI and gives also a textual description

body_mass  = float(input("Body mass in kilograms:"))
heigth = float(input("heigth in meters:"))
bmi = body_mass / (heigth * heigth)
if(bmi < 18.5):
    print("category Underweigth")
elif(bmi >= 30):
    print("category Obesity")
elif(bmi < 25):
    print("category Normal Weigth")
else:
    print("category Overweigth")

# 4. User gives a month number and our program tells the number of days in that month

month_number = int(input("month by number:"))
if(month_number % 2 == 0):
    print("days: 31")
else:
    print("days: 30")

# 5. User gives the lengths of the triangle's sides. Program tells what the triangle like (rigth angle)

side_left = int(input("Give left side of triangle:"))
side_bot = int(input("Give bottom side of triangle:"))
side_rigth = int(input("Give bottom side of triangle:"))

a = 0
b = 0
c = 0

if(side_left > side_bot):
    if(side_rigth > side_bot):
        c = side_bot
        a = side_rigth
        b = side_left
    else:
        c = side_rigth
        a = side_bot
        b = side_left
elif(side_rigth > side_left):
    c = side_left
    a = side_bot
    b = side_rigth
else:
    c = side_rigth
    a = side_bot
    b = side_left

math_ab = a * a + b * b
if(math_ab == c*c):
    # rigth angle 90 degrees : a^2 + b^2 = c^2
    print("rigth angle triangle")
elif(math_ab < c*c):
    # obtuse one angle over 90 : a^2 + b^2 < c^2
    print("obtuse angle")
else:
    # acute, all angles under 90 : a^2 + b^2 > c^2
    print("acute angle")


# 6. Variables a, b and c have different values. Create a program that finds the biggest one ( 3 different ways)

a = int(input("1. Number:"))
b = int(input("2. Number:"))
c = int(input("3. Number:"))

max_number = 0

# first
if(a > b):
    if(a > c):
        max_number = a
    else:
        max_number = c
elif(b > c):
    max_number = b
else:
    max_number = c

print(max_number)

# second
max_number = max(a, b, c)
print(max_number)

# third
values = [a, b ,c]
max = values[0]
for i in range(1, 3):
    if values[i] > max :
        max = values[i]

print(max)