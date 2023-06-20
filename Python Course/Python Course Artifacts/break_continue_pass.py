#break = terminate loop

while True:
    name = input("Enter your name: ") 
    if name != "":
        break 
#continue = skip to next iteration of loop
phone_number = "804-456-4455"

for i in phone_number:
    if i == "-":
        continue
    print(i, end = "" )
print("\n")

#make your own program: superstitious snakes
#take x and y from user, display with commas and spaces (no comma at end); exclude 13
x = int(input("Minimum: "))
y = int(input("Maximum: "))

for i in range(x,y+1):
    if i == 13:
        pass 
    elif i <= y-1:
        print(i, end =", ")
    else: 
        print(i, end = "")