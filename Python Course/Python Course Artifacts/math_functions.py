import math
#math module

pi = 3.14
print(round(pi)) #round to the nearest whole integer
print(math.ceil(pi)) #round to the highest integer
    #NB: need to call math module for special function
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(pi))

x = 1
y = 2
z = 3
print("The largest value among the variables is: "+str(max(x,y,z)))
    #NB: also works for min
