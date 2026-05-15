#data of my self
name="rehan" #my name
age=16 #my age
height=5.7 #my height
relationship="self" #relationship self
print("name:",name)
print("age:",age)
print("height:",height)
print("relation:",relationship)
print("_________________________________________________________")
#data of my brother
name1="zeeshan" #name of my brother
age1=20 #age of my brother
height1=5.7 #height of my brother
relationship1="brother" #relationship brother
print("name:",name1)
print("age:",age1)
print("height:",height1)
print("relation:",relationship1)
print("___________________________________________________________")
#data of my sister
name2="bushra" #name of my sister
age2=22 #age of my sister
height2=5.3 #height of my sister
relationship2="sister" #relationship sister
print("name:",name2)
print("age:",age2)
print("height:",height2)
print("relation:",relationship2)
print("______________________________________________________________")
#data of my father
name3="khalid" #name of my father
age3=48 #age of my father
height3=5.6 #height of my father
relationship3="father" #relationship father
print("name:",name3)
print("age:",age3)
print("height:",height3)
print("relation:",relationship3)
print("________________________________ ________________")

name="rehan"
age=16
adress=182
pincode=1100025
phoneno=9891074798
print("name:",name)
print("age:",age)
print("adress:",adress)
print("pincode:",pincode)
print("phoneno:",phoneno)

age=float(input("Enter the age"))
print("age of user:",age)
if age<60:
  print("not senior citizen")
else:print("senior citizen")

a=str(110025)
lenght_a=len(a)
print("length of a:",lenght_a)

age=18
if age >=18:
  print("you can vote")
else:
  print("too young to vate")


marks=float(input("enter the marks to deside the grade"))
if  marks >=90:
  grade="A"
elif marks >=75:
  grade="B"
elif marks >= 60:
  grade="c"
else:
  grade="D"
print(f"Grade:{grade}")


nn     c=float(input("temp in calcius"))
f=(c*9/5)+32
print(f"temp in frrundheight {round(f)}")


year=int(input("enter year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(f"{year} is a leap year.")
else:
  print(f"{year} is a not leap year.")


#data of the f-strng fantion
  name="rehan"
height=5.7
print("my name is",name)
print("my height is",height)
print("__________________________________________________")
print(f"my name is {name} and my height is {5.7}")
school="gbsss"
city="delhi"
hobby="gaming"
print(f"my school name is {school} and my city is {city} and my {hobby}")


#arithmatic useing fstring opration
a=7
b=8
print(f"sum of {a} and {b} is {a+b}")
print(f"minus of {a} and {b} is this {a-b}")
print(f"multi of {a} and {b} is this {a*b}")
print(f"divide of {a} and {b} is this {a/b}")

a=189
print(f"table of {a}")
print(f"{a}*1:{a*1}")
print(f"{a}*2:{a*2}")
print(f"{a}*3:{a*3}")
print(f"{a}*4:{a*4}")
print(f"{a}*5:{a*5}")
print(f"{a}*6:{a*6}")
print(f"{a}*7:{a*7}")
print(f"{a}*8:{a*8}")
print(f"{a}*9:{a*9}")
print(f"{a}*10{a*10}")


#get two number from user
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
#calculation
sum_result=num1+num2
diff_result=num1-num2
prod_result=num1*num2
quot_result=num1/num2
#display using f-string
print(f"sum: {num1}+{num2} = {sum_result}")
print(f"difference: {num1}-{num2} = {diff_result}")
print(f"product: {num1}*{num2} = {prod_result}")
print(f"Quotient: {num1}/{num2} = {quot_result}")

a1=int(input("enter the user"))
for i in range (1,11):
  print(i*a1)

  from ast import Name
Names=["rehan,zeeshan,bushra,khalid"]
ages=[16,21,24,45]
heights=[5.7,5.7,5.1,5.6]
print("names:",Names)
print("ages:",ages)
print("heights:",heights)
for name in Names:
  print("name:",name)


name="rehan"
for i in name:
 print(i)

 sum=0
a=int(input("enter the first number"))
b=int(input("enter the second number"))
for i in range (a,b):
  sum=i+sum
  print(i)

  for i in range(13,55):
 print(i)

 l1=[5,4,8,17,32]
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])
print(l1[4])

l1=[5,4,8,17,32]
lenght=len(l1)
print("lenght of the list:",lenght)
for i in range(0,lenght):
  print(l1[i])

  l1=[5,4,8,17,32,45,56,76,21]
lenght=len(l1)
print("lenght of the list:",lenght)
for i in range(0,lenght,2):
  print(l1[i])

  #simple interest calculator
principal=float(input("enter principal ammount:"))
rate=float(input("enter rate of interest:"))
time=float(input("enter time (years):"))

simple_interest=(principal*rate*time)/100
print(f"simple interst: {simple_interest:.2f}")

l1=[4,5,6,4,3,8,5.6,11.5,22.4,34.5,6.7]
even=[]
odd=[]
for l in l1:
  print("elementery:",l)
  if l%2==0:
    even.append(l)
  else:
    odd.append(l)
print("even list:",even)
print("odd list:",odd)

hours = float(input("Enter hours: "))

minutes=hours*60
seconds=hours*3600

print("Minutes:",minutes)
print("Seconds:",seconds)



num=int(input("enter user number"))
num2=float(input("enter user number"))
print("converted into int:",num)
print("converted into float:",num2)



numbers_str = "10,20,30"
parts=numbers_str.split()
print("parts:",parts)
total=0
for p in parts:
  total += int(p)
print("sum =",total)

num=563487
#num = int(input("Enter number: "))
is_prime = num > 1
for i in range(2,int(num**0.5)+1):
    print("i:",i)
    if num % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not Prime")



n = int(input("Enter n:"))
total = 0
for i in range(1,n+1):
  total=total+i
print("total:",total)


a = float(input("First number: "))
b = float(input("Second number: "))
if b == 0:
    print("Cannot divide by zero")
else:
    print(f"Result = {a/b:.2f}")

    for i in range(1,11):
    for j in range(1,11):
        print(f"{i*j:4}",end="")
    print()



    numbers_str = "10 20 30"
parts=numbers_str.split(" ")
print("parts:",parts)
print("type of parts:",type (parts))
total=0
for p in parts:
  print(p)
  total += int(p)
print("sum =",total)




l1=[12,23,34,45,43.2,23,5.2,"rehan"]
l_int=[]
l_str=[]
for l in l1:
  if str==type(l):
   if int==type(l):
      l_int.append(l)
      l_str.append(l)
print("l_int:",l_int)
print("l_str:",l_str)


n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")


num = int(input("Enter an integer: "))
total = 0
temp = abs(num)   # handle negative numbers
while temp > 0:
    total += temp % 10    # get last digit
    temp //= 10           # remove last digit
print(f"Sum of digits = {total}")


n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    n = int(input("How many Fibonacci numbers? "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b   # simultaneous update
print()


# String iteration
name = "Python"
for char in name:
    print(char)



    for i in range(49, 0, -4):
    print(i)


    from os import remove
fruits = ["apple","mango","banana","orenge"]

for fruit in fruits:
    print(f"I like {fruit}")


    num=
while num <= 0 and len(str(num))==6:
  num=int(input("enter a positive number:"))
  if num <= 0:
    print("that's not positive.try again.")
print(f"thank you: you entered {num}.")


start = int(input("enter countdown start:"))
while start > 0:
  print(start)
  start -= 2
print("blast off;")


for i in range(3,0,-1):
  for r in range(3,0,-1):
    print(f"({i}, {r})",end=" ")
  print()


  rows = 5
for i in range(1, rows +1):
  for j in range(i):
    print(i, end=" ")
  print()



  rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()



    for i in range(1,10):
  if i == 5:
    break
  print(i)

  for num  in range(1,11):
  if num % 2 != 0:
     continue
  print(num)

  num = 29
for i in range(2, int(num ** 0.5) + 1):
  if num % i == 0:
    print(f"{num} is not prime.")
    break
else:
    print(f"{num} is prime.")




print("prime numbers between 1 and 50:")
for num in range(2, 51):
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        break
  else:
      print(num, end=" ")





      import random

secret = random.randint(1, 200)
attempts = 0
max_attempts = 10

print("welcome to the number guessing game!")
print(f"guess a number betweeen 1 and 100. you have {max_attempts} attempts.")

while attempts < max_attempts:
  guess = int(input("your guess: "))
  attempts += 1

  if guess < secret:
      print("too low! try again. ")
  elif guess > secret:
     print("too high! try again. ")
  else:
      print(f"correct! you guesses it in {attempts} attempts. ")
      break

else:
     print(f"out of attempts! the number was {secret}. ")
___________________________________________________________________________________________________-



