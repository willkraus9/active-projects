#index operator [] = access to elements in string, list, tuples

name = input("What is your name?: ")

if (name[0].islower()):
    name = name.capitalize()
    print(name)

#make it your own: where is the space?
    #search for space between first and last name, print separately + capitalize
space = name.find(" ")
    #parentheses bc not in index --> in string!!!
first_name = name[:space].upper()
last_name = name[space+1:].lower()
last_char = name[-1]
    #have to add 1 bc inclusionary at beginning of array call, exclusionary at end
print(first_name)
print(last_name)
print(last_char)

