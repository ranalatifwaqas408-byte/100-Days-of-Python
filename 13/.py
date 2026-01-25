class Car:
    num_wheels=4
    gas=30
    headlights=2
    size='tiny'
    def __init__(self,make,model):
        self.make=make
        self.model=model
        self.wheels=Car.num_wheels
        self.gas=Car.gas

    def drive(self):
        if self.wheels<Car.num_wheels or self.gas <=0:
            return 'Cannot Drive'
        self.gas-=10
        return self.make+" "+self.model+"gose vroom"

    def fill_gas(self):
        self.gas+=20
        return 'Gas level:' + str(self.gas)

deneros_car=Car('Tesla','Model S')
print(deneros_car.model) 
deneros_car.gas = 10 
print(deneros_car.drive()) 
print(deneros_car.drive()) 
print(deneros_car.fill_gas()) 
print(deneros_car.gas) 
print(Car.gas) 
deneros_car=Car('Tesla','Model s') 
deneros_car.wheels=2 
print (deneros_car.wheels) 
print(Car.num_wheels) 
print(deneros_car.drive()) 

# print(Car.drive()) 

print(Car.drive(deneros_car))


class MonsterTruck(Car): 
    size = 'Monster' 
    
    def rev(self): 
        print("Vroom! This Monster Truck is huge!")

    def drive(self): 
        self.rev() 
        return super().drive()
deneros_car = MonsterTruck('Monster', 'Batncbile') 
print(deneros_car.drive())
print(Car.drive(deneros_car)) 
print(MonsterTruck.drive(deneros_car)) 

# Car.rev(deneros_car)

class MarksCounter:
    def __init__(self, marks_dict):
        self.marks = marks_dict  # store marks in a dictionary

    def GetMarks(self, name):
        # Return marks if name exists, else None
        return self.marks.get(name)

    def AddMarks(self, name, additional_marks):
        if name in self.marks:
            self.marks[name] += additional_marks
            print(f"{name} just earned {additional_marks} more marks!")
            print(f"Now he has {self.marks[name]} marks")
        else:
            # If student not in dict, you could initialize or ignore; based on output, we assume they exist
            pass

    def GetHighestMarks(self):
        # Return name of student with highest marks
        if not self.marks:
            return None
        highest_name = max(self.marks, key=lambda k: self.marks[k])
        print(f"{highest_name} has the highest marks")
        return highest_name