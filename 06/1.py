x=input("Enter student first name:")
y=input("Enter student middle name:")
z=input("Enter student last name:")
print()

print("")
marks1=float(input(("Enter marks of Urdu:")))
marks2=float(input("Enter marks of English:"))
marks3=float(input("Enter marks of Mathematics:"))
marks4=float(input("Enter marks of Physics:"))            

total_marks=marks1+marks2+marks3+marks4

if(total_marks>80 and total_marks<90):
 print("The student has passed with grade A")

elif(total_marks<80 and  total_marks>70 ):
 print("The student has passed wih grade B")

elif(total_marks<70 and total_marks>50):
 print("The student has passed with grade C")

elif(total_marks<40):
 print("The student has not passed\n Grade F  ")

while total_marks:
 if total_marks<=40:
  print("The student will not repeat ")
 else:
  print("The student will repeat")
  break


  


 
