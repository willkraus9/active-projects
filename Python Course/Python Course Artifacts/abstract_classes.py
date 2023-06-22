#abstract - prevent user creating object for class
    #abstract class = contains >=1 abstract method
    #abstract method = method has declaration but not implementation

from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod #can't make any more vehicle classes + can't create objects 
    def go(self): 
        pass
class Car(Vehicle):
    def go(self):
        print("Drive the car")
        #needs the go method now!!! Can't run without overriding all methods from parent class
class Motorcycle(Vehicle):
    def go(self):
        print("Ride the motorcycle")
        
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()
        