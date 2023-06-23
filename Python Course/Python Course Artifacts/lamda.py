# lambda function = func written in one line and use lambda keyword
    #accept any number of arguemnts, but only one expression
    #lambda parameters:expression

def double(x):
    return x*2
#instead, do this!
double=lambda x:x*2
print(double(5))

multiply = lambda x,y:x*y
print(multiply(5,2))
add = lambda x,y,z: x+y+z
print(add(5,6,7))

full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Will","Kraus"))

age_check = lambda age: True if age >= 18 else False
print(age_check(23))