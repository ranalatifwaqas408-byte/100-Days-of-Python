marks=[3,5,6,"Latif",True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

colours=["green","blue","red","yellow","black"]
print(colours)
print(colours[3])
print(colours[-3])

if "3" in marks:
    print("Yes")
else:
    print("no")
    if "tif" in "Latif":
        print("Yes")

animals=["dog","cat","bat","lion","tiger","donkey","zebra","monkey","parrot","elephant"]
print(animals)
print(animals[2:8])
print(animals[0:-1])


l=[1,2,3,4]                     
print(l)
l.append(7)
print(l)

l=[11,45,67,9,6,89,7,-8,78,-65,76,-54]
print(l)
l.sort(reverse=True)                          
print(l)                                    

l=[1,4,8,0,6,5,5,3,2,8]
print(l)                                    
print(l.count(8))
print(l)