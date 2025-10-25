tup=(1,2,4,6,8,"green")
print(type(tup),tup)
print(tup[0])
print(tup[5])
print(len(tup))
if 4 in tup:
    print("Yes it is present")

animals=("cat","dog","bat","mouse","pig","horse","donkey","cow")
print(animals[1:7:3])

                                #    tuples methods
countries=("Spain","Italy","Pakistan","England","Germany")
temp=list(countries)
temp.append("Russia")                              #add item
temp.pop(3)                                       #remove item
temp[2]="Finland"                                 #change item
countries=tuple(temp)                                
print(countries)

countries1=("Pakistan","Afghanistan","Bangladesh","SriLanka")
countries2=("Vietnam","India","China")
SouthEastAsia=countries1+countries2
print(SouthEastAsia)


tuple3=(0,1,2,3,4,3,8,7,3,2,3)
res=tuple3.count(3)                                #count tuple
print('count of 3 in tuple3 is:',res)

tuple4=(0,1,3,7,8,8,5,1,4,1,3,1,1)
prep=tuple4.index(1,4,9)
print("index of 1 in tuple4 is:",prep)                     #index tuple9