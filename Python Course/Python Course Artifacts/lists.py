#lists - store multiple items in single variable (aka arrays)

food = ["pizza", "sushi", "hamburger","hotdog","spaghetti"]
food[0] = "chips"
#print(food[0])
    #NB: arrays start at 0!

for x in food:
    print(x)

food.append("ice cream")
    #adds something to the end of the array
food.remove("hotdog")
    #removes SPECIFIC item from list
food.pop()
    #removes last item in array
food.insert(0,"cake")
    #replace one item with another
food.sort()
    #sorts the array alpabetically
food.clear()
    #removes the entire list