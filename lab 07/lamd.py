# Program 1
def interest_calculator(rate):
    return lambda principal:principal+principal*rate

# Program 3
def make_adder(n):
    return lambda x:x+n

# Program 2
larger = lambda a, b: a if a > b else b


def print_table(n, upto):
    for i in range(1, upto+1):
        print(n, "x", i, "=", n * i)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

big = larger(a, b)
print("Larger number is:", big)

limit = int(input("Enter table limit: "))
print_table(big, limit)


# Program 4
def menu(choice):
    if choice == "1":
        return lambda:"Hello! Welcome!"
    elif choice == "2":
        return lambda x:x**2
    elif choice == "3":
        def reverse_string(s):
            return s[::-1]
        return lambda s:reverse_string(s)
    else:
        return lambda:"Invalid Choice"
    
    # Program 5

    def operation_menu(choice):
        if choice == "A":
            return lambda x:x-5
        elif choice == "B":
            return lambda x:x*5
        elif choice == "C":
            return lambda x:x**5
        else:
            return lambda :"Invalid Choice"
        
        # Program 6
        