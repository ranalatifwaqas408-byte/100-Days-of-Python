#program 1

a=float(input("enter 1st num: "))
b=float(input("enter 2nd num: "))
def calculator(a,b):
    add=a+b
    sub=a-b
    return add,sub
print('add and sub are:',calculator(a,b))

# program 2

def is_armstrong(x):
    digits=str(x)
    total=sum(int(digit)**3 for digit in digits)
    return total==x
print(is_armstrong(153))

#program 3
def lucky_number(limit):
    for i in range(1,limit+1):
        if i %7==0 and i % 10 ==7:
            print(i)

#program 4
def binary_decimal(binary_str):
    dec=0
    power=0
    for digit in binary_str[::-1]:
        dec += int(digit) * (2 ** power) 
        power += 1 
        return dec 

 # program 5
def spy_num(n):
    s=0
    p=1 
    temp = n 
    while temp > 0:
        d = temp % 10 
        s += d 
        p *= d 
        temp // 10 
    return s==p 

# program 6
def power(base,exp):
    result=1 
    for i in range(exp):
        temp=0
        for i in range(base):
            temp += result 
        result = temp 
    return result 

# program 7
def gcd_lcm(a,b):
    x,y = a,b 
    while y !=0:
        x,y = y,x%y 
    gcd = x 
    lcm = (a,b)// gcd 
    return gcd,lcm 

#program 8
def largest_in_range(numbers):
    largest = numbers [0]
    for n in numbers:
        if n> largest :
            largest= n 
    return largest 

# program 9
def bmi_category(weight,height):
    bmi = weight / (height * height)
    if bmi < 18.5 :
        return "underweight"
    elif bmi < 24.9:
        return "normal"
    elif bmi < 29.9:
        return "overweight"
    else:
        return "obese"