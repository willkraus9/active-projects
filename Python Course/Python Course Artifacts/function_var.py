def hello():
    print("Hello")

print(hello) #prints where function is in computer's memory
hi = hello #not calling function
#print(hi) #same memory address
hi() #therefore calls hello function

say = print
say("Woah!")
