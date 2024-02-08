import random

#1 Program calculates the sum of values 1 - 5. Use: for and while

sum = 0

for x in range(6):
    sum += x

print(sum)
sum = 0
x = 0

while(x < 6):
    sum += x
    x = x + 1
print(sum)

#2 Program calculates the sum of even numbers between 2 - 40. Use: for and while 
sum = 0
for x in range(2 , 40, 2):
    sum += x
print(sum)

x = 0
sum = 0
while(x < 41):
    if(x % 2 == 0):
        sum += x
    x = x + 1

print(sum)
#3 Program calculates sum: 5, 10, 15, .. 100. Use: for and while 
sum = 0
for x in range(5 , 105, 5):
    print(x)
    sum += x
print(sum)

sum = 0
x = 5
while(x < 101):
    if(x % 5 == 0):
        sum += x
    x = x + 1
print(sum)

#4 Program throws dice 100 times and tells amounts of different values 
#(1, 2, 3, 4, 5, and 6). Hints: from random import randint ( scaling example [0,10] value = randint(0, 10) )

numbers_one = 0
numbers_two = 0
numbers_three = 0
numbers_four = 0
numbers_five = 0
numbers_six = 0

for x in range(101):
    value = random.randint(1, 6)
    if(value == 1):
        numbers_one = numbers_one + 1
    if(value == 2):
        numbers_two = numbers_two + 1
    if(value == 3):
        numbers_three = numbers_three + 1
    if(value == 4):
        numbers_four = numbers_four + 1
    if(value == 5):
        numbers_five = numbers_five + 1
    if(value == 6):
        numbers_six = numbers_six + 1
print(numbers_one, "ones," , numbers_two, "twos," , numbers_three, "threes," , numbers_four, "fours," , numbers_five, "fives," , numbers_six, "Sixes")

# 5 Account manager with menu: User can make deposits Do withdrawal Check the balance
deposit = 0
while(True):
    print("press 1 to deposite, press 2 to withdraw or press 3 to check balance")
    print("Press anything else to quit transaction")
    option = input("choice:")
    if(option == 1):
        deposit = int(input("Amount deposit:"))
    elif(option == 2):
        deposit = deposit - int(input("Amount withdraw:"))
        # time to go for debt
    elif(option == 3):
        print(deposit)
    else:
        break
   
 
# 6 Try to solve this equation (try find 1 of roots) 3x^3 - 4x^2 + 9x +5 = 0 Here ^ means exponent
#import numpy ...
a = 3
b = 4
c = 9
d = 5


Q = (3 * a * c - b ** 2)/(9 * (x **2))

R = (9 * a * b * c - 27 *( a ** 2) - 2 * (b**3))/(54 * (a ** 3) )

partial_root = (Q ** 3 + R ** 2) ** (1/2)
S = (R + partial_root) ** (1/3)
T = (R - partial_root) ** (1/3)

Root = S + T -( b / (3 * a))
#???
print(Root)
#7 Print this kind of semipyramid (character amount of rows is given in a variable):
#m 
#mm 
#mmm 
#mmmm 
#mmmmm

rows = int(input("rows of m: "))
x = 0
ms = "m"
for x in range(rows):
    print(ms)
    ms = ms + "m"
#8. Program calculates the factorial of n (given in a variable)

number = int(input("factor for number: "))
x = 0
factorial = 1
for x in range(number):
    factorial *= (x + 1)

print(factorial)
#9. Program calculates the exponential value (base and exponent are given in a variable). Base can be a real number, exponent is a whole number. Use a loop.

base = int(input("base number: "))
exponent = int(input("exponent number: "))
solution = 1
for x in range(exponent):
    solution *= base
print(solution)