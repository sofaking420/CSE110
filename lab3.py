# -*- coding: utf-8 -*-
"""lab3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uUUcayUORwJPX2360Wdsfo616PRf423n
"""

#task1(a)
counter = 24
while counter>=-6:
    if counter ==-6:
        print(counter, end="")
    else:
        print(counter, end=", ")
    counter = counter-6

#task1(b)
counter = -10
while counter<=20:
  if counter==20 :
    print(counter, end="")
  else:
    print(counter, end=", ")
  counter+=5

#task1(c)
counter = 18
while counter<=63:
  if counter==63:
   print(counter,end="")
  else:
   print(counter,end=", ")
  counter+=9

#task1(d)
counter = 18
while counter<=63:
      if counter%2!=0:
        if counter==63:
          print(-1*counter,end="")
        else:
          print(-1*counter,end=",")
      else:
        print(counter,end=",")
      counter = counter+9

#task2
car=str(input())
number=int(input())
for i in range(number):
    print(car)

#task3
a= 0
for i in range(1,601):
    if i%7==0 and i%9==0:
         a=a+i
print(a)

#task4
a= 0
for i in range(1,601):
    if i%7==0 and i%9==0:
      pass
    elif i%7==0 or i%9==0:
      a=a+i
print("total:",a)

#task5
for i in range(10,51):
  if i%2!=0:
    print(i,end=" ")

#task6
num1=int(input("Please enter num1 number: "))
sum2=0
for i in range(1,num1+1):
    if i%2!=0:
        sum2+=(i**2)
    else:
        sum2-=(i**2)
print(sum2)

#task7
sum=0
count=0
for value in range(0,10):
     number=int(input("Enter number: "))
     if number%2==0:
         pass
     else:
         count=count+1
         sum=sum+number
average=sum/count
print("The total of odd number is",sum,"and their average is",average)

#task8
number=int(input("Enter a number: "))
x=1
sum=0
while x<=number:
    if x%7==0:
        sum=sum+x
    x=x+1
print(sum)

#Task-09
n=1
sum=0
while n!=6:
    number=int(input("Enter a number: "))
    n=n+1
    sum=sum+number
    print(sum)

#Task-10
number=int(input("Enter your number: "))
while number!=0:
    last_num=number%10
    if last_num%number==0:
      print(last_num,end="")
    else:
      print(last_num,end=",")
    number=number//10

#task11
num = int(input("Please enter a number: "))
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " ,str(count))

#task12
number = int(input("Please enter a number: "))
temp =number
count=0
while temp!=0 :
  temp=temp//10
  count+=1

power=10**(count-1)

while number>0:
  digit= number // power
  number = number%power
  power = power//10
  if power!=0:
    print(digit,end=",")
  else:
    print(digit,end="")



#n = int(input("Enter: "))
#count = 0
#num1 = n
#while num1 != 0:
#    num1 = num1 // 10
#    count += 1
#power = (10 ** (count - 1))
#while n > 0:
#    number = n // power # get first digit
 #   n = n % power
 #   power = power // 10
 #   if n == 0:
 #       print(number,end="")
 #   else:
 #       print(number,end = ",")

#task12
n = int(input("Enter: "))
count = 0
num1 = n
while num1 != 0:
    num1 = num1 // 10
    count += 1
power = (10 ** (count - 1))
while n > 0:
    number = n // power # get first digit
    n = n % power
    power = power // 10
    if n == 0:
        print(number,end="")
    else:
        print(number,end = ",")

#task16
quan = int(input("please enter the quantity: "))
count = 0
sum =0
while count<=quan:
  number = int(input("Please enter the number: "))
  sum+=number
  if count==1:
    maximum_number = number
    minimum_number = number
    count+=1
  else:
    if number<minimum_number:
      minimum_number = number
    elif number>maximum_number:
      max_number = number
  count+=1
average = sum/quan
print("Maximum",maximum_number)
print("Minimum", minimum_number)
print("Average",average)

#task13
count = 0
number = int(input("Please enter a number: "))
for i in range (1,number+1):
  if number%i==0:
    count+=1
    print(i)
print("Total",count,"Divisions")

#task14
sum = 0
temp = int(input("Please enter a number: "))


for i in range(1,temp+1):
  if temp%i==0:
    sum+=i

if sum-temp==temp:
  print(temp,"is a perfect number")
else:
  print(temp,"is not a perfect number")

#task15
count = 0
number1 = int(input("Please enter a number: "))
for i in range (1,number1+1):
    count+=1
if count<=2:
  print(number1,"is a prime number")
else:
  print(number1,"is not a prime number")

#task17
n=int(input())
for i in range(n):
    for j in range(n):
        print("+",end="")
    print()

#task18
n=int(input())
m=int(input())
for i in range(n):
    for j in range(1,m+1):
        print(j,end="")
    print()

#task19
num1=int(input())
for i in range(1,num1+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

n=5
for i in range(1,n):
  for j in range(1,i):
      print(j)
  print()

i=18
while i <=63:
  if i==63:
    print(i)
  elif i%2==0:
    print(i,end=",")
  else:
    print(-i,end=",")
  i=i+9

num_1=int(input("Please enter a number: "))
sum=0
i=1
while i<=n:
  sign= (-1)**(i-1)
  term=sign*i**2
  sum+=term
  i+=1
print(sum)

#random
sum=0
while True:
    message = input("please enter number or enter stop: ")
    if message=="stop":
        break
    sum += int(message)
print(sum)

#task9
sum1=0
for i in range(5):
    a = int(input("Please enter a number: "))
    sum1+=a
    print("output",sum1)

#task2
car_name = str(input("please enter ur car name: "))
number = int(input("please enter a number: "))
count = 0
while count<number :
  print(car_name)
  count+=1

#task25
number = int(input())
number2 =
fibonacci = 0
while number :
  print(number)