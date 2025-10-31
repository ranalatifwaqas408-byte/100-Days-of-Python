def factorial(n):
 if(n==0 or n==1) :
  return 1
 else:
  return n*factorial (n-1)
print(factorial(3))
print(factorial(6))
print(factorial(8))
print((factorial(10)))
        

#   fibonacci series      
a, b = 0, 1
print("Fibonacci series less than 100:")

while a < 100:
    print(a, end=" ")
    a, b = b, a + b