class Car: 
    color = None

class Motorcycle:
    color = None
def change_color(car,color):
    car.color = color
    
car1 = Car()
car2 = Car()
car3 = Car()
bike1 = Motorcycle

change_color(car1,"red")
change_color(car2,"white")
change_color(car3,"blue")
change_color(bike1,"black")