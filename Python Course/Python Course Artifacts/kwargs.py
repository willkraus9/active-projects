#kwargs = key word arguments = pack args into dictionary instead of tuple
    #can get into keyword arguments

def hello (**kwargs):
    print("Hello, " +kwargs["first"] +" " +kwargs["middle"] +" " + kwargs["last"])
    print("Hello,", end = " ")
    for key,value in kwargs.items():
        print(value, end=" ")
hello(title = "Mr.", first = "Will", middle = "J.", last = "Kraus")
    
