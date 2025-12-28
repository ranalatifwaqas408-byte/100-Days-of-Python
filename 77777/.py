n = int(input("Enter number: "))
i = 1

while i <= n:
    print(i)
    i += 1

def prime(n):
    if n <= 1:
        return "Not Prime"

    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

print(prime(7))

n = int(input("Enter number: "))
rev = 0

while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n //= 10

print("Reverse =", rev)
n = int(input("Enter terms: "))
a = 0
b = 1

print(a)
print(b)

for i in range(2, n):
    c = a + b
    print(c)
    a = b
    b = c


a = int(input("Enter base: "))
b = int(input("Enter power: "))
p = 1

for i in range(b):
    p = p * a

print("Result =", p)
