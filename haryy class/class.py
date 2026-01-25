# class Person:
#     name="Harry"
#     occupation="Software Developer"
#     networth=10
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

#         a=Person()
#         a.name="rohan"
#         a.occupation="accountant"
#         a.info()

# 
# email = "user@example.com"
# domain = email.split('@')[-1]
# print(domain)
# name = "John Ronald Reuel Tolkien"
# abbr = "".join([word[0].upper() + "." for word in name.split()])
# print(abbr)
# def factorial(n):
#     res = 1
#     for i in range(1, n + 1): res *= i
#     return res
# print(factorial(6))  
# 


# t = t + (4,)t = (1, 2, 3)
# print(t)

lst = [1, 2, 3]
rev = []

for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])

print(rev)
