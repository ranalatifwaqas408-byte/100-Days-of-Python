count=5
while(count>0):
    print(count)
    count=count - 1
    #Question#2
    for i in range(12):
        print("5 X",i+1,"=",5*(i+1))
        if(i==10):
            break

# Question#3

for i in range(12):
    if(i==10):
        print("Skip the iteration")
        continue
    print("5 X",i,"=",5*i) 

# Question#4
for i in range(1,101,1):
    print(i,end=" ")
    if(i==50):
     break
    else:
       print("Mississippl")
       print("Thank You")
    

for i in[2,3,4,6,8,0]:
    if(i%2!=0):
        continue
    print(i)

i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break