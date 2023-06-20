#dictionary = changeable unordered collection of unieque key value pairs
    #fast bc use hashing
    #uses colons to separate instead of commas (diff from sets)
            #curly braces, just like as in sets

#countries and their capitals
capitals = {"USA": "Washington, DC",
            "India": "New Delhi",
            "China": "Beijing", 
            "Russia": "Moscow"}
print(capitals["Russia"])
    #don't have to use index number for this one
    
print(capitals.get("Germany"))
    #check to see if there is a key in dictionary

print(capitals.keys())
    #print only the keys
print(capitals.values())
    #print only the values
print(capitals.items())
    #print all
    
#can change after the program is running
capitals.update({"Germany": "Berlin"})
