# -*- coding: utf-8 -*-
"""lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wWOz3e57jz4oPZuoYxkESghh3MLOzN_y
"""

#task1
a=  int(input())
b= int(input())
sum = a+b
Product= a*b
difference = a-b
print(f"Sum={sum} Product={Product} Difference={difference}")

#task2
import math
var_1 = float(input("Please enter a number: "))
area = math.pi*var_1**2
circ = 2*math.pi*var_1
print("Area is",area)
print("Circumference is",circ)

#task3
num1 = int(input('Please enter first number: '))
num2 = int(input('Please enter second number: '))
if num1>num2:
  print('First is greater')
elif num1<num2:
  print("Second is greater")
else:
  print("The numbers are equal")

#task4
num1 = int(input("please enter a number: "))
num2 = int(input("please enter a number: "))
if num2>num1 :
  answer= num2 - num1
elif num2<num1 :
  answer= num1 - num2
elif num1==num2:
  answer= num1-num2
print(answer)

#task5
a = int(input("Please enter a number: "))
if a%2 == 0:
  print("The number is even")
elif a!=2 :
  print("The number is odd")

#task6
a= int(input())
if a%2==0 or a%5==0 :
    print(a)
else:
    print("Not a multiple of 2 OR 5")

#task7
a = int(input())
if a%2==0 and a%5==0:
  print("Multiple of 2 and 5 both")
elif a%2==0 or a%5==0:
  print(a)
else:
  print("Not a multiple we want")

#task8
a=int(input("Please enter a number: "))
if a%2==0 and a%5==0 :
    print(a)
else:
    print("Not multiple of 2 and 5 both")

#task 9
a = int(input())
hour = a//3600
b=a%3600
c = a//60
min = c%60
s=a%60
print("Hours:",hour,"Minutes:",min,"Seconds:",s)

#task10
h= int(input("Please enter a number: "))
if 0<=h<=168:
    if h<=40 and h>=0:
        sal=h*200
        print(sal)
    elif 40<h<=168:
        sal =8000+(h-40)*300
        print(sal)
elif h<0:
    print("Hour cannot be negative")
else :
    print("Impossible to work more than 168 hours weekly")

#task11
import math
s= int(input("Please enter a number: "))
if s<100:
    l1 = 3000-(125*(s**2))
    print(l1)
elif s>=100:
    l2=12000/(4+((s**2)/14900))
    print(l2)

#task12
hour= int(input("Please enter a hour: "))
if hour <0 or hour >23:
    print("Wrong time")
else:
    if hour >=4 and hour <=6:
        print("Breakfast")
    elif hour >=12 and hour <=13:
        print("Lunch")
    elif hour >=16 and hour <=17:
        print("Snacks")
    elif hour >=19 and hour <=20:
        print("Dinner")
    else:
        print("Patience is a virtue")

#task13
numbers=int(input("Please enter a number: "))
if numbers>=90:
    print("A")
elif 80<=numbers<=89:
    print("B")
elif 70<=numbers<=79:
    print("C")
elif 60<=numbers<=69:
    print("D")
elif 50<=numbers<=59:
    print("E")
else:
    print("F")

#task14
distance = int(input("Please enter a number: "))
time = int(input("Please enter a time: "))
speed = (distance/1000)/(time/3600)
if speed<60 :
    print(speed, "km/h")
    print("Too slow. Needs more changes")
elif 60<=speed<=90:
    print(speed,"km/h")
    print("Velocity is okay. The car is ready!")
elif 90<speed :
    print(speed, "km/h")
    print("Too fast. Only a few changes should suffice.")

#task15
cgpa=float(input("Please enter a number: "))
credit = int(input("Please enter a number: "))
if credit>=30:
    if 3.80<=cgpa<=3.89:
        print("The student is eligible for a waiver of 25 percent.")
    elif 3.90<=cgpa<=3.94:
        print("The student is eligible for a waiver of 50 percent.")
    elif 3.95<=cgpa<=3.99:
        print("The student is eligible for a waiver of 75 percent.")
    elif cgpa==4.00:
        print("The student is eligible for a waiver of 100 percent.")
else:
    print("The student is not eligible for a waiver" )

num_1 = int(input("Please enter a number: "))
if num_1%2==0 or num_1%5==0:
  print("NO")
else:
  print(num_1)

i = int(input())
if i%3==0 and i%5==0:
    print("FizzBuzz")
elif i%3==0:
    print("Fizz")
elif i%5==0:
    print("Buzz")
else:
    print(i)

a= int(input())
if a%2==0 and a%5==0:
    print("No")
else:
    print(a)

#task20
num_1 = int(input("Please enter a number: "))
if num_1%2==0 and num_1%5==0 :
  print("No")
elif num_1%2==0 or num_1%5==0:
  print("No")
else:
  print(num_1)

num_1 = int(input("Please enter a number: "))
if num_1%2==0 and num_1%5==0 :
  print("No")
else:
  print(num_1)

canvas = int(input("Please enter a number: "))
paint = int(input("Please enter a number: "))
sum = 120*