#args = pack all arguments into tuple (ordered, unchangeable)

def add(*stuff):
    #the asterisk is where the *args comes in!
    sum = 0
    #cast tuple as a list so that can modify inside function:
    stuff = list(stuff)
    for i in stuff:
        sum+=i
    return sum

print(add(1,2,3,4,5,6,7,8))
