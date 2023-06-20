import time
#for loop: execute block of code for a limited amount of time
    #while loops = unlimited for loop (while loop maybe not needed)

for i in range(10): #executes 10 times, starting at 0 and excluding 10
    print(i+1) #starts at 1 now, goes to 10
    
for i in range(50,100+1,2):
    print(i)

#can also iterate through name too!
for i in "Will Kraus":
    print(i)
    
#simulate countdown

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")