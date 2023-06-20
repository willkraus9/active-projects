#logical operators (and,or): check if operation = true 

temp = int(input("What is the temp outside?: "))

if temp >= 0 and temp <=30:
    print("The temp is good today.")
    print("Go outside!")
elif temp <0 or temp >30:
    print("It's bad outside today.")
    print("Stay inside!")
#not operator: can reverse entire logic by surrounding not(var args)
