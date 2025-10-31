s={2,4,6,3,2}
print(s)
info={"Carla",19,False,5.9,19}
print(info)

latif=set()
print(type(latif))
for value in info:
 print(value)

#set methods
s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
s1.update(s2)                   #here update method adds elemts of s2 in s1
print(s1,s2)



cities1={"Tokyo","London","Lahore","Delhi"}
cities2={"Islamabad","Beijing","Lahore","Madrid"}
cities3=cities1.difference(cities2)                            
print(cities3)


cities4={"New York","Berlin","Gujrat","Jakarta"}
cities5={"Berlin","Cairo","Bangkok","Souel"}
print(cities4.issuperset(cities5))
