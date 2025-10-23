# Task1
#Sum of natural number entered by User
#Using While loop

x=int(input("Enter a Number: "))
total=0
i=1
while (i<=x):
    total += i
    i+=1 
print("Sum is:",total)

#Task2
#Multiplication Table

x=int(input("Enter a number: "))

for i in range(1,11):
    result=x*i
    print(f'{x}x{i}={result}')
    
#Task3
#Factorial of given number

num=int(input("Enter a number: "))
factorial=1
while num>0:
    factorial*=num
    num=num-1
print("The factorial is",factorial)

#Task4
#reversing the given integer

x=int(input("Enter integer: "))
reverse_number=0
temp=x

while temp>0:
    digit=temp%10
    reverse_number=reverse_number*10+digit
    temp=temp//10
print(f'original:{x} \n reversed:{reverse_number} ')
    
    
#Task 5
#Counting and displaying numbers

x=int(input("Enter a Number: "))
count=0
temp=x
while temp>0:
    count+=1
    temp=temp//10
print(f'Number of digits in {x} are {count}')

#Task6
#stars

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()  

#Task7
#Secret number

secret_num=7
attempt=0

while True:
    guess= int(input("Enter a secret number(1-10): "))
    attempt+=1
    if guess==secret_num:
       print("The secret number is correct: ")
    break
else:
    print("Try Again")

    
#Task8
#Fibonacci sequence

Term=int(input("Enter number of terms: "))
a,b=0,1
print("fibonacci sequence:")
for i in range(Term):
    print(a,end="")
    a,b=b,a+b