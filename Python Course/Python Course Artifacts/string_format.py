#string.format = give more control about display output

animal = "Cow"
item = "Moon"

#print("The " +animal +" jumped over the " +item)

print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))
    #prints in index form: positional argument
print("The {animal} jumped over the {item}".format(animal="Cow", item="Moon"))
    #keyword argument: choose variable for FORMAT FIELD stated in format section after string

text = "The {} jumped over the {}"
print(text.format(animal,item))

name = "Will"
print("Hello, my name is {:10}".format(name))
    #ten spaces of room for format variable (makes 10 spaces)
    #left align: {:<##}
    #right align: {:>##}
    #center align {:^##}

number = 3.14159
print("The number pi is  {:.2f} ".format(number))
    #will round number to 2 decimal places, f = float
        #:b = binary, :x = hexadecimal, :e = sci notation

