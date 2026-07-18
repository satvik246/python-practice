age=20
price=10.5
first_name="Satvik"
is_online=True
print(first_name)

#Exercise
patient_name="John Smith"
age=20
is_newPatient=True

name=input("What is your Name ? ")
print("Hello "+name)

birth_year=input("What is your birth year ? ")
age=2026-int(birth_year)
print(age)
#types of casting
#int()
#float()
#str()
#bool

first_num=input("First :")
second_num=input("Second :")
total=float(first_num)+float(second_num)
print("Sum is : " + str(total))
#need to use float if there are any decimal values ..int only works with whole numbers

age=int(input("age : "))
age=age+25
print("age is " + str(age))
#Need to be careful while using + symbol , we cannot use it with one string and one number both of them needs to be of same type



#Below are the string operations
course="Python For Beginners"
print(course.upper())
print(course)
print(course.find('For'))
print(course.replace('For','4'))
print("Python" in course)

#Below are the arithemetic operations
print(2+3)
print(10-3)
print(10*2)
print(10**2)
print(10/4)
print(10//4) #acting like trunc in oracle sql
x=10
x+=3 #augmented arithemetic operation
print(x)

#Comparision operatiors
# >,<,>=,<=,==,!=
x=3>2
x=3<2
x=3==3
print(x)

#Logical Operators
x=5
print(x<10 and x>5)
print(x==5 or x>10)
print(not x==5)

temperature=25
if temperature>30 :
  print("It's a hot day")
  print("Drink Plenty Of Water")
elif temperature > 20 :
  print("It's a Nice Day")

print("done")

weight=float(input("Weight : "))
unit = input("(K)g or (L)bs : ")
unit = unit.upper()
if unit == 'K' :
  final_wt = weight * 2.205
  print("Weight in lbs is : " + str(final_wt))
elif unit == 'L' :
  final_wt = weight / 2.205
  print("Weight in kg is : " + str(final_wt))

sal=int(input("Please Enter your Salary : "))
bonus_per=int(input("Please enter your bonus Percentage : "))
bonus_amt=(sal*bonus_per)/100
total_sal = bonus_amt+sal
print("The total salary is : " + str(total_sal))

i=1
while i<=5 :
  print(i)
  i=i+1

i=1
while i<=10:
  print (i * '*')
  i=i+1

#lists in python used to store list of objects
#list methods : append , insert , remove , clear - will delte the elemetns inlist
names=["satvik","shiva","venkata","kunala"]
print(names)
names[0]='SATVIK'
print(names[0:3])
names.append('Mom')
print(names)
names.append(1)
print(names)
names.insert(0,10)
print(names)
print(1 in names)
print(len(names))

numbers=[1,2,3,4,5]
for item in numbers :
  print(item)
#using join
numbers=[1,2,3,4,5] 
print(f"Items : {', '.join(map(str,numbers))}")

# 3rd parameter in range is used to skip the numbers
numbers = range(0,10,3)
for number in numbers :
  print(number)

# Lists in square braces , tuples in round braces
numbers = (1,2,3,4)
print(numbers)
print(numbers.count(3)) #counts the accurance of mentioned value
print(numbers.index(2)) # return the index of provided value
print(numbers(1)) # note that tuples are not callable unlike in lists

#Multiplication Program Exercise
num  = int(input("Please enter a number : "))
for i in range(1,11) :
  print(str(num) + '*' + str(i) + '= ' + str(num * i))

#list of 5 city names
cities = ['hyderabad','mumbai','delhi','chennai','banglore']
print(cities[0])
print(cities[-1])
cities.append('Vizag')
cities.remove('mumbai')
print(cities)
print(len(cities))

