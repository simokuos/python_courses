from random import choices
from random import randint
import math
# 1. Array contains 30 random values. calculate sum and average
   
test_list = choices(range(0, 100), k = 30)
list_sum = 0
for x in range(30):
    list_sum =list_sum + test_list[x]

average = list_sum/30
print(list_sum)
print(average)
# 2. Find the max of array
max = test_list[0]
for x in range(30):
    if(max < test_list[x]):
        max = test_list[x]

print("max: ", max)

# 3. search value from array

value = int(input("search for value in list:"))

for x in range(30):
    if(value == test_list[x]):
        value_index = test_list[x]
        print(value, " was in list and is found at index: ", value_index)


# 4. fill 2 arrays with some values calc sum array

list_a = choices(range(0, 10), k = 10)
list_b = choices(range(0, 10), k = 10)

list_sum = [list_a[x] + list_b[x] for x in range(10)]

# 5. Generate a lottorow

list_all = [x for x in range(0, 40)]
#print(list_all)
n = len(list_all)
lottorow=[]
for x in range(1,8):
    y = randint(0, n - x)
    element = list_all.pop(y)
    lottorow.append(element)

print(lottorow)
# 6. https://docs.python.org/3/tutorial/datastructures.html create examples of methods

list_male_names = ["garen", "sylas","carl"]
list_female_names = ["annie", "sarah","neeko"]
list_names = ["annie", "sarah"]
list_male_names.append("subaru")
list_female_names.insert(1, "subaru")
list_archived = list_names.copy()

list_names.clear()
list_names.extend(list_male_names)
list_names.extend(list_female_names)
print(list_names.count("subaru"))
list_names.remove(list_names[list_names.index("subaru")])
print(list_names)
list_names.sort()
print(list_names)
list_names.reverse()
print(list_names)

# 7. Short dictionary, word pairs
fin_eng_dictionary = {
  "torni" : "tower",
  "joki"  : "river",
  "tonttu": "Elf",
  "kääpiö": "dwarf",
  "taika" : "magic",
  "parta" : "beard",
  "miekka": "sword",
  "tikku" : "stick", 
}
#There are 20 values in an array: calculate the standard deviation
#2 arrays contain students grades in math and in English language. There are 10 students. Try to calculate the correlation.
math_grades = choices(range(4, 11), k = 10)
eng_grades = choices(range(4, 11), k = 10)
all_grades = math_grades + eng_grades

#standard deviation

avr_grades = sum(all_grades) / len(all_grades)
temp_list = [x - avr_grades for x in all_grades]
for x in range(len(temp_list)):
    temp_list[x] = temp_list[x] ** 2

avr_variance = sum(temp_list)/(len(all_grades) -1)
print("standard deviation of grades is ", math.sqrt(avr_variance))

#correlation 
grades = math_grades.copy()  
math_avr_grades = sum(grades) / len(grades)
temp_list = [x - math_avr_grades for x in grades]
for x in range(len(temp_list)):
    temp_list[x] = temp_list[x] ** 2

avr_variance = sum(temp_list)/(len(grades) -1)
math_dev = math.sqrt(avr_variance)

grades = eng_grades.copy()  
eng_avr_grades = sum(grades) / len(grades)
temp_list = [x - eng_avr_grades for x in grades]
for x in range(len(temp_list)):
    temp_list[x] = temp_list[x] ** 2

avr_variance = sum(temp_list)/(len(grades) -1)
eng_dev = math.sqrt(avr_variance)
dif_sum = 0;
for i in range(len(math_grades)):
    x = math_grades[i]
    y = eng_grades[i]
    print("x ", x ,"y ", y)
    dif_sum += (x - math_avr_grades) * (y - eng_avr_grades)

print(dif_sum)
correlation = dif_sum/(eng_dev * math_dev)
correlation_grades = correlation / 19
print("correlation: " , correlation_grades)