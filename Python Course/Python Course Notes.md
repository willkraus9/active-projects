# Python Full Course for free 
## Link: https://www.youtube.com/watch?v=XKHEtdqhLK8

# Loops: for loops, if statements, while loops
## If Statements
* age = int(input("How old are you?: "))
* if age ==100:
* print("You are a century old!")

## Logical Operators 
* if temp >= 0 and temp <=30:
* print("The temp is good today.")
* elif temp <0 or temp >30:
* print("It's bad outside today.")
  
## For Loops
* for i in range(50,100+1,2): #range: start, end, step; end = exclusionary --> add 1
* print(i)

### Nested For Loops
* rows = int(input("How many rows?: "))
* columns = int(input("How many columns?: "))
* symbol = input("Symbol type?: ")
* for i in range(rows):
* for j in range(columns):
* print(symbol, end = "")
* #after print symbol, enter new line character (bc use column)
* print() #printing new line, have to be in rows loop!!!

## While loops
* name= ""
* while len(name) ==0:
* name = input("Enter your name: ")
* print ("Hello, "+name)

## Break, Continue, Pass
### Break = terminate loop
* while True:
* name = input("Enter your name: ") 
* if name != "":
* break 
### Continue = skip to next iteration of loop
* for i in "804-456-4455":
* if i == "-":
* continue
* print(i, end = "" )
### Pass = skip loop ouptut
* #take x and y from user, display with commas and spaces (no comma at end); exclude 13
* x = int(input("Minimum: "))
* y = int(input("Maximum: "))
* for i in range(x,y+1):
* if i == 13:
* pass 
* elif i <= y-1:
* print(i, end =", ")
* else: 
* print(i, end = "")

# Iterable Types: Lists(1D, 2D), Dictionaries, Tuples, Sets
## Lists: brackets + comma separation
* food = ["pizza", "sushi", "hamburger","hotdog","spaghetti"]
* food[0] = "chips"
* #functions: .append = add something new to end of array, .remove = remove specific item, .insert(index, "replace"), .sort = alphabetically, .clear = remove list

### Walrus operator (:=) - assign value to variables 
* foods = list()
* while food := input("What food do you like?: ") !="quit":
* foods.append(food)

### Filter lists using Lambda function
* friends = [('Rachel',19), ('Monica',18), ('Phoebe',17)]
* age = lambda data:data[1]>=18
* drinking_buddies = list(filter(age, friends))

### Better list: list variable = [expression for item in iterable]
* better_squares = [i*i for i in range(1,11)]
* print(better_squares)

## Lists (2D) -  combine lists to form lists of lists
* drinks = ["Coffee", "Soda", "Tea"]
* dinner = ["Pizza", "Hamburger", "Hotdog"]
* dessert = ["Cake", "Ice Cream"]
* food = [drinks,dinner,dessert]
* print(food[0][1]) # first list, second list, all

### Sort lists by characteristics
* students = ["Squidward",'Sandy','Patrick','Spongebob','Mr. Krabs']
* students.sort() #alphabetical order, reverse for (reverse=True)
* student_record = [('Squidward','F',60),('Sandy','A',33),('Patrick','D',36),('Spongebob','B',20),('Mr. Krabs','C',78)]
* #sort by grade or age
* grade = lambda grades:grades[1]
* age = lambda grades:grades[2]

## Dictionaries - curly braces + separated by colon; keys then values
* capitals = {"USA": "Washington, DC", "India": "New Delhi", "China": "Beijing", "Russia": "Moscow"}
* print(capitals["Russia"])
* #check for key: print(capitals.get("Germany"))

### Convert to celsius in new dictionary:
* cities_in_F = {'New York':32,'Boston':75,'Los Angeles':100,'Chicago':50}
* cities_in_C = {key: round((value-32)*5/9) for (key,value) in cities_in_F.items()}

## Tuples = ordered + unchanging arrays (uses parentheses)
* student = ("Bro", 21,"male")
* print(student.count("Bro"))

### Combine iterables with zip (creates tuple)
* usernames = ['Mister','Dude','Bro']
* passwords = ('p@ssword','abc223','guest')
* #get both iterable in pairs
* users = dict(zip(usernames,passwords))
* for key,value in users.items():
* print(key+" : "+value)

## Sets - unordered, unindexed; uses curly braces
* utensils = {"fork","spoon","knife"}
* for x in utensils:
* print(x)
* utensils.add("napkin")
* utensils.remove("fork")
* utensils.update(dishes) #dishes = new set
* dinner_table = utensils.union(dishes) #puts two sets together under new name
* print(utensils.difference(dishes)) #what utensils has but dishes doesn't
* print(utensils.intersection(dishes)) #what utensils and dishes both have



# Strings
* print("\n") # new line
* name = input ('what is your name?: ") # User inputs - gain variables from command line

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

## String slicing with index [start:stop:step]
* reversed_name = name[::-1]
* website2 = "http://wikipedia.com"
* #create substring site name: slice = slice(7,-4)
* #negative index (char most on right = -1, etc.)

## Index Operator: call elements of a string, list, tuple, etc.
* name = input("What is your name?: ")
* #search for space between first and last name, print separately + capitalize
* space = name.find(" ")
* first_name = name[:space].upper()
* last_name = name[space+1:].lower()
* last_char = name[-1]

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

### Moving where strings are printed: 
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

# Multiprocessing (run processes in parallel)

## Multiprocessing w/ counting
* from multiprocessing import Process, cpu_count
* import time
* def counter (num):
* count = 0
* while count < num:
* count +=1
* def main():
* a = Process(target = counter,  args = (500000000,))
* b = Process(target = counter, args = (500000000,))
* b.start()
* a.start()
* a.join()
* b.join()
* print("Finished in ",time.perf_counter(),"seconds.")            
* if __name__ == 'main':
* main()

## Multithreading
* #thread in computer engineering: flow of executing instructions
* #each take a turn running due to GIL (1 thread running at one time)
* #tasks can either be cpu bound or io bound:
* #cpu bound = program waiting for internal events (better to use multiprocessing)
* #io bound = waiting for external (user input, web scraping, etc.)
* import threading
* import time
* print(threading.active_count())
* print(threading.enumerate())
* #can have one thread for input, another for countdown timer
* def eat_breakfast():
* time.sleep(3)
* print('You finished breakfast')
* def drink_coffee():
* time.sleep(4)
* print('You drink coffee')
* def study():
* time.sleep(5)
* print('You finish studying')    
* x = threading.Thread(target = eat_breakfast, args=())
* x.start()
* y = threading.Thread(target = drink_coffee, args=())
* y.start()
* z = threading.Thread(target = study, args=())
* z.start()
* eat_breakfast()
* drink_coffee()
* study()

# File Manipulation

## Reading Files
* try:
* with open('C:\\Users\\WillKraus\\Documents\\Personal Lists\\List_6_21.txt') as file:
* print (file.read())
* #NB: works only if in same folder if just listing document!
* except FileNotFoundError:
* print("The file does not exist.")

## Writing Files 
* with open('test.txt','a') as file: #"r" = read, 'a' = append(add new stuff)
* text = "Have a great day!"
* file.write(text) #this creates the file inside the current folder

## Delete Files
* import os
* os.remove('') #write out file path except if in project folder

## Detect Files
* import os 
* path = "C:\\Users\\WillKraus\\Documents\\Personal_Lists\\List_6_21.txt"
* if os.path.exists(path):
* print("That location exists!")
* if os.path.isfile(path):
* print("That is a file.")
* else:
* print("That location does not exist.")

## Move Files
* import os
* source = " "
* destination = " "
* #move file from source to destination
* try: 
* if os.path.exists(destination):
* print("There's a file already there")
* else:
* os.replace(source,destination)
* print(source+ " was moved.")
* except FileNotFoundError:
* print(source+ " was not found.")

# Libraries
## import random
* myList = ["rock", "paper","scissors"]
* z = random.choice(myList)
* cards = [1,2,3,4,5,6,7,8,9,10, "J", "Q", "K","A"]
* random.shuffle(cards)
* print(cards[0])

## import functools
* letters = ['H','E','L','L','O']
* word = functools.reduce(lambda x,y: x+y,letters)

## import keyword_arg
* #if __name__ = '__main__'  (what does it do?)
* #module (python script) can be run as own program, can be imported to other modules
* import keyword_arg
* print(keyword_arg.__name__)

## import time
* print(time.ctime(1000000))
* print(time.time()) #return current seconds since epoch
* time_object = time.localtime()
* local_time = time.strftime('%B %d %Y %H:%M:%S',time_object) 

## import math 
* pi = 3.14
* print(round(pi)) #round to the nearest whole integer
* print(math.ceil(pi)) #round to the highest integer
* print(math.floor(pi))
* print(abs(pi))
* print(pow(pi,2))
* print(math.sqrt(pi))

## import modules (your own module)
* modules1.hello()
* modules1.bye()
* from modules1 import hello, bye #could also do import all = *
* hello()
* bye()

# GUI (Graphical User Interface): widget=element, window=container

## Basic structure: 
* from tkinter import *
* window = Td()
* ~~whatever you are trying to import
* ~~variable.pack
* window.mainloop()

## Labels
* from tkinter import *
* window = Tk()
* #photo = PhotoImage(file='xxx')
* label = Label(window,text = "Hello world!",font = ('Times New Roman', 40,'italic'), fg = '#00FF00', bg = 'black',relief = RAISED,bd = 10, padx =20, pady=20)#image = photo, compound='bottom'
* label.pack()
* #label.place(x=0,y=0)
* window.mainloop()

## Buttons
* from tkinter import *
* def click():
*     print("you clicked the button!")
* window = Tk()
* button = Button(window, text = "click me", command = click,font = ("Comic Sans",30), fg ="#00FF00",bg = 'black',activeforeground='#00FF00',activebackground='black')
* button.pack()
* window.mainloop()

## Windows
* from tkinter import *
* #widgets = GUI elements, windows = container for widgets
* window = Tk() #instantiate an instance of a window
* window.geometry('420x420')
* window.title("Will GUI Window")
* #can change icon if in project folder
* #icon = PhotoImage(file = 'filename')
* #window.iconphoto(True, icon)
* window.config(background='black')
* window.mainloop() #place window on computer screen, listen to events

## Radio Buttons (bubble-in type)
* from tkinter import *
* food = ['pizza','hamburger','hotdog']
* window = Tk()
* x = IntVar()
* def order():
* if(x.get()==0):
* print("You ordered pizza.")
* elif(x.get()==1):
* print("You ordered hamburger.")
* else:
* print("You ordered hotdog.")
* for index in range(len(food)):
* radiobutton = Radiobutton(window,text = food[index],variable = x,value = index,padx=25,font = ("Impact",50),command =order #set command of radiobutton to function)
* radiobutton.pack(anchor=W)
* window.mainloop()

## Checkbox
* from tkinter import *
* def display():
* if (x.get() ==1):
* print("You agreed.")
* else:
* print("You don't agree.")
* window = Tk()
* x = IntVar() #StringVar = return string (look at more!)
check_button = Checkbutton(window,text = 'Do you agree?',variable = x, #1 or 0
* onvalue = 1,offvalue = 0,command = display) 
* check_button.pack()
* window.mainloop()

## Entry Box (text appears, deletes, submits, clears)
* from tkinter import *
* def submit():
* username = entry.get()
* print("Hello, "+username)
* def delete():
* entry.delete(0,END)
* def backspace():
* entry.delete(len(entry.get())-1, END)
* window = Tk()
* entry = Entry(window, font =('Comic Sans', 50))
* entry.pack(side = LEFT)
* submit_button = Button(window, text = "submit", command = submit)
* submit_button.pack(side = RIGHT)
* delete_button = Button(window, text = "delete", command = delete)
* delete_button.pack(side = RIGHT)
* backspace_button = Button(window, text = "backspace", command = backspace)
* backspace_button.pack(side = RIGHT)
* window.mainloop()

