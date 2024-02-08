import math
from random import sample 
from random import randint 
#create functions and run tests
# 1. returns average of 2 integers
def average2Ints(x, y):
    average = (x + y)/2
    return average
# 2. returns average of 4 floating point values
def average_four_arg(a, b, c, d):
    average = (a + b + c + d)/2
    return average
# 3. returns sum of array
def arraySum(array):
    answer = sum(array)
    return answer
# 4. returns factorial
def Factorial(n):
    answer = sum(range(1, n + 1))
    return answer
# 5. returns biggest of 3 int
def max_of_three(x, y, z):
    if(x < y):
        if(y < z):
            answer = z
        else:
            answer = y
    elif(x < z):
        answer = z
    else:
        answer = x
    return answer
# 6. returns the bmi, ask 2 numbers?
def BMI_calculator(body_mass, heigth):
    bmi = body_mass / (heigth * heigth)
    return bmi
# 7. returns biggest of five integers
def max_of_five(a, b, c, d, e):
    temp_list = [a, b, c, d, e]
    max_number = a
    for x in range(len(temp_list)):
        if(max_number < temp_list[x]):
            max_number = temp_list[x]
    return max_number
# 8. calculates ammount of combinations(use earlier factorial function)
def combinationCalculation(unique_objects_amount, unique_set_size):
    a = unique_objects_amount
    b = unique_set_size
    answer = Factorial(a)/(Factorial(b)*Factorial(a - b))
    return answer
# 9. calculates standard deviation
def standardDeviation(list_of_numbers):
    averages = sum(list_of_numbers) / len(list_of_numbers)
    temp_list = [x - averages for x in list_of_numbers]
    for x in range(len(temp_list)):
        temp_list[x] = temp_list[x] ** 2
    variance = sum(temp_list)/(len(list_of_numbers) -1)
    return math.sqrt( variance )
# 10. value from array
def searchValue(array, value):
    for x in range(len(array)):
        if(value == array[x]):
            value_index = x
            return value_index
    print("not in list")
    return -1
# 11. Calculates the square root of value 2 (create your own function)
def root_of_2():
    start = 0
    number = 2
    end = number
    while(start<=end):#not neccesary for this, useful for logic for other roots
        mid = (start + end)/2
        if(mid * mid == number):
            ans = mid
            break
        if(mid * mid < number):
            ans = start
            start = mid + 1
        else:
            end = mid - 1
    increment = 0.1
    for x in range(5):
        while(ans * ans <= number):
            ans += increment
        ans = ans - increment
        increment = increment / 10
    print(ans)
# 12. Calculates an approximation of Neper's value (e).
def calcNepersValue():
    ans = 1.0
    for x in range(1, 31):
        a = 1/Factorial(x) 
        print(a)
        ans = ans + a  
    print(ans)#decimal accuracity in counting phase too low
# 13. Calculates approximations of sin(x) and cos(x)
def calcSinAndCos(n):
    sin = n
    cos = 1
    base_cos = 2
    base_sin = 3
    increment = 0
    minus = -1
    cos = 0.0
    sin = 0.0
    for x in range(16):
        cos = cos + minus * ( n ** (base_cos + increment) / Factorial(base_cos + increment))
        sin = sin + minus * ( n **(base_sin + increment) / Factorial(base_sin + increment))
        increment += 2
        minus = minus * -1
    print(cos)
    print(sin)



#testing functions
test_list = [x for x in range(10)]
print(average2Ints(test_list[0], test_list[1]))
print(average_four_arg(test_list[0], test_list[1], test_list[2], test_list[3]))
print(arraySum(test_list))
print(Factorial(test_list[4]))
print(max_of_three(test_list[0], test_list[1], test_list[2]))
print(BMI_calculator(test_list[8], test_list[9]))
print(max_of_five(test_list[0], test_list[1], test_list[2], test_list[3],test_list[4]))
print(combinationCalculation(len(test_list), randint(1,10)))
print(standardDeviation(test_list))
print(searchValue(test_list, randint(1,10)))
root_of_2()
calcNepersValue()
calcSinAndCos(randint(1,10))

test_list = sample(range(31), 20)

print(average2Ints(test_list[0], test_list[1]))
print(average_four_arg(test_list[0], test_list[1], test_list[2], test_list[3]))
print(arraySum(test_list))
print(Factorial(test_list[4]))
print(max_of_three(test_list[0], test_list[1], test_list[2]))
print(BMI_calculator(test_list[8], test_list[9]))
print(max_of_five(test_list[0], test_list[1], test_list[2], test_list[3],test_list[4]))
print(combinationCalculation(len(test_list), randint(1,10)))
print(standardDeviation(test_list))
print(searchValue(test_list, randint(1,10)))


