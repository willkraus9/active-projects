#input() = get input from user in command line
    #NB: have to run Python file instead of code

name = input("What is your name?: ")
#NB: always going to be a string, so typecast
    #have to be either int or float
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))
    #by having a float here, can accept decimals
print("Hello "+name)
print("Your are " +str(age)+ " years old")
    #NB: have to be string in this case bc displaying strings together
print("You are " +str(height)+ " cm tall")
