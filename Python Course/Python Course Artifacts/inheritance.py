#inheritance - "child" class inherit attributes from "parent" class
class Animal: #parent: what all have in common
    alive = True
    
    def eat(self):
        print("This animal is eating")
    def sleep (self):
        print("This animal is sleeping")
        
class Rabbit(Animal):#child: what are different
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.swim()
hawk.fly()
