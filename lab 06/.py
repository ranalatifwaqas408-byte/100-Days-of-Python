# Question 1
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
def calculator(a,b):
    addition=a+b
    subtraction=a-b
    return addition,subtraction
print("Addition and Subtraction are:",calculator(a,b))

# Question 2
for i in range(3):
    for j in range(2):
        print(i, j)
x = 3
y = 2.0
print(type(x / y))
print(int(y))

a = 'Hi'
b = 'There'
print(a + b * 2)

a='you'
b='are'
c='fine'
print(a,b*3,c*2)
a = int(input("Enter number: "))
b = int(input("Enter another: "))
print("Sum is:", a + b)

count = 0
while count < 3:
    print("Counting:", count)
    count += 1

x = 0.1 + 0.2
if x == 0.3:
    print("Equal")
else:
    print("Not equal")
x = 5
def change():
    global x
    x = x + 1
    print(x)
change()
