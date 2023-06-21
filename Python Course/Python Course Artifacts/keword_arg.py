#keyword arguments = arguments preced by identifier when calling
    #instead of relying on order for receiving functions, can get identifier to identify where variable goes

def hello(first, middle, last):
    print("Hello, " +first +" " +middle +" "+last)
    
hello(last = "Kraus", middle="J.", first = "Will")
