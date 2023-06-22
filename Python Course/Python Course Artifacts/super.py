#super() - get methods of parent class (return object of parent class)
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
        
class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
        #code is reused from previously declared parent class
class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def volume(self):
        return self.length*self.width*self.height
    
square = Square(3,3)
cube = Cube(3,3,3)
rectangle = Rectangle(4,2)
print(rectangle.area())
print(square.area())
print(cube.volume())
#NB: when printing, need to have () after calling attribute!