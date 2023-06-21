#use programming to define what objects are
    #attributes (what objec is or has)
    #methods (what object can do)
class Car: #should be capital
    #attributes:
    make = None
    model = None
    year = None
    color = None 
    #methods:
    def drive(self):
        print("This "+self.model+" is driving!")
    def stop (self):
        print("This "+self.model+" is stopped.")
    def __init__ (self, make, model, year, color):#assign attributes via initialize method
        self.make = make
        self.model = model
        self.year = year
        self.color = color
#from car import Car (if from another Python file with classes)
car_1 = Car("Chevy","Corvette","2021","Blue")
car_2 = Car("Ford","Mustang","2022","Red")
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()
car_1.stop()
