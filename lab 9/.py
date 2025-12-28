#Lab 9


#program 1

def interest_calculator(rate):
    return lambda principal:principal+principal*rate

b=interest_calculator(5)
print(b(10))

#Program 2

a=lambda x,y:x if x>y else y
c=a(4,5)
print(c)
def table(a):
    for i in range(1,11):
        z=int(c)*i
        print(f'{c}*{i}={z}')

table(a)

#Program 3

def make_adder(n):
    return lambda e:n+e

d=make_adder(5)
print(d(4))

#Program 4

def menu(choice):
    if choice=="1":
        return lambda:"Welcome"
    elif choice=="2":
        return lambda b:b**2
    elif choice=="3":
            return lambda s:s[::-1]
    else:
        print("Value Error")
menu(5)
#  Program 5

def cal_GPA():
    subjects=int(input("Enter Subjects: "))
    cum_grade_point=0
    total_credit_hours=0
    for i in range(1,subjects+1):
        print(">>subject",i)
        x=float(input("Grade points= "))
        y=int(input("Credit hours: "))
        total_grade_point=x*y
        cum_grade_point+=total_grade_point
        total_credit_hours+=y

    GPA=cum_grade_point/total_credit_hours
    return GPA

print(cal_GPA())


#Lab 10

#Program 1

x=list(input("Enter a List: "))
l=[]
for i in x:
    if i not in l:
        l.append(i)
print(l)

#Program 2

def small(l):
    l.sort()
    element=l[1]
    return element

print(small([3,45,5,6,7,2,3]))

#Program 3

def intersection(t1,t2):
    intersection_tup=()
    temp1=list(t1)
    temp2=list(t2)
    for i in temp1:
        if i in temp2:
            intersection_tup+=(i,)

    return intersection_tup
t1=(1,2,3,4,5)
t2=(1,2,3,6,7)

print(intersection(t1,t2))

#Program 4 

matrix = []
for i in range(3):
    row = input(f"Enter row {i+1} (space-separated): ").split()
    matrix.append([int(x) for x in row])

for row in matrix:
    print(row)

print("Transpose of the Matrix:")
for row in zip(*matrix):
    print(list(row))