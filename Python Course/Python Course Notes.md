# Python Full Course for free 
## Link: https://www.youtube.com/watch?v=XKHEtdqhLK8

# Iterables: Lists (1D, 2D), Dictionaries, Tuples
## Lists
* #filter lists using Lambda function: 
* friends = [('Rachel',19), ('Monica',18), ('Phoebe',17)]
* age = lambda data:data[1]>=18
* drinking_buddies = list(filter(age, friends))

## Lists (2D) - have solid brackets + comma separation, combine lists of lists
* drinks = ["Coffee", "Soda", "Tea"]
* dinner = ["Pizza", "Hamburger", "Hotdog"]
* dessert = ["Cake", "Ice Cream"]
* food = [drinks,dinner,dessert]
* print(food[0][1]) # first list, second list, all

## Dictionaries - curly braces + separated by colon; keys then values
* capitals = {"USA": "Washington, DC", "India": "New Delhi", "China": "Beijing", "Russia": "Moscow"}
* print(capitals["Russia"])
* #check for key: print(capitals.get("Germany"))
* #convert to celsius in new dictionary:
* cities_in_F = {'New York':32,'Boston':75,'Los Angeles':100,'Chicago':50}
* cities_in_C = {key: round((value-32)*5/9) for (key,value) in cities_in_F.items()}

## Tuples = ordered + unchanging arrays
* student = ("Bro", 21,"male")
* print(student.count("Bro"))

# User inputs - gain variables from command line
name = input ('what is your name?: ")

# Printing strings
## Searching in strings
* name = "Will"
* print (name.find("W"))
* #first = 0
* print(name.lower())
* print(name.isdigit())
* print(name.isalpha())
* print(name.count("l"))
* #replace some letters in name variable 
* print(name.replace("i","a"))

## String slicing with Index #index [start:stop:step]
* reversed_name = name[::-1]
* website2 = "http://wikipedia.com"
* #create substring site name: slice = slice(7,-4)
* #negative index (char most on right = -1, etc.)

## Type Casting - make variables into specific types 
* print(str(y))
* print(int(x))
* print(float(z))
* print('You are ' +str(age) +' years old')
## Formatting strings - different ways of printing variables
* animal = "Cow"
* item = "Moon"
* print("The {} jumped over the {}".format(animal, item))
* print("The {0} jumped over the {1}".format(animal, item))
* #prints in index form: positional argument
* print("The {animal} jumped over the {item}".format(animal="Cow",item="Moon"))
* text = "The {} jumped over the {}"
* print(text.format(animal,item))
* name = "Will"
* print("Hello, my name is {:10}".format(name))
* #ten spaces of room for format variable (makes 10 spaces)
* #left align: {:<##}
* #right align: {:>##}
* #center align {:^##}
* number = 3.14159
* print("The number pi is  {:.2f} ".format(number))
* #will round number to 2 decimal places
* #:f = float, :b = binary, :x = hexadecimal, :e = sci notation

# Exception handling: input from user = bad
* try: #if a user input might not allow code to run
* numerator = int(input("Enter a number to divide: "))
* denominator = int(input("Enter a number to divide by: "))
* result = numerator/denominator
* except ZeroDivisionError as f:
* print(f)
* print("You can't divide by zero!")
* finally: #always execute no matter what
* #can close files here
* print("Thank you for using the calculator!")

