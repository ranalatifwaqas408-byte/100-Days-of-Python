#TASK 1

def rem(l):
    nl=[]
    for elem in l:
        if elem not in nl:
            nl.append(elem)

    return nl
print(rem([1,2,3,4,2,3,5,3,6,7,4,2]))

#TASK 2
l1=list(input("Enter list: "))
l2=list(input("Enter list: "))
lnew=[]
for elem in l1:
    if elem in l2:
        lnew+=[elem]
print(lnew)

#TASK 3
def rem(l):
    la=[]
    for elem in l:
        if elem!=0:
            la+=[elem]
    return la

print(rem([1,2,3,40,9,0,67,0,5,3,0]))

#TASK 4

def chng(t):
    temp=list(t)
    e=int(input("enter index to change element: "))
    d=int(input("enter changed element: "))
    temp[e]=d
    temp2=tuple(temp)
    return temp2

t=(1,2,3,4)
print(chng(t))


#TASK 5

t=("a","abg","qwer")
longest=t[0]
for elem in t:
    if len(elem)>len(longest):
        longest=elem

print("longest string:", longest)

#TASK 6

def same(t1,t2):
    temp1=list(t1)
    temp2=list(t2)
    temp1.sort()
    temp2.sort()
    if temp1==temp2:
        return True
    else:
        return False
    
t1=(1,5,3,4)
t2=(1,4,3,5)
print(same(t1,t2))