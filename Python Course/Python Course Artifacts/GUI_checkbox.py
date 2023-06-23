from tkinter import *

def display():
    if (x.get() ==1):
        print("You agreed.")
    else:
        print("You don't agree.")
window = Tk()
x = IntVar() #StringVar = return string (look at more!)
check_button = Checkbutton(window,
                           text = 'Do you agree?',
                           variable = x, #1 or 0
                           onvalue = 1,
                           offvalue = 0,
                           command = display) 
check_button.pack()


window.mainloop()