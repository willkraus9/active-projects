#method chaining - call methods sequentially (OOP)
    #each call performs action on same object and returns self
class Car:
    def turn_on(self):
        print("Start the car")
        return self
    def drive(self):
        print("Drive the car")
        return self
    def brake(self):
        print("Push the breaks")
        return self
    def turn_off(self):
        print("Stop the car")
        return self
car = Car()
car.turn_on().drive()
car.brake().turn_off()
#NB: this format only works if you have "return self" after each attribute!