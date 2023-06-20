#nested loop: 1 loop inside another loop

#set width, height for output command line

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Symbol type?: ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end = "")
        #after print symbol, enter new line character (bc use column)
    print() #printing new line