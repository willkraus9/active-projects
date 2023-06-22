class Animal:
    def eat(self):
        print("This animal is eating")
class Rabbit(Animal):
    pass
    def eat (self):
        #provide more specific implementtiaon class as parent 
        print("This rabbit is eating a carrot")
rabbit = Rabbit()
rabbit.eat()