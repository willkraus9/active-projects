#exception = event detected that interrupts flow program
try: #if a user input might not allow code to run
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as f:
    print(f)
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("Enter only numbers!")
except Exception:
    print("something went wrong")
    #NB: should have more than one exception!
    #Exceptions execute in the order in which they are defined (zero divide by = first; if not, then next one)
        #catch additional exceptions before running code
else:
    print(result)
finally: #always execute no matter what
    #can close files here
    print("Thank you for using the calculator!")