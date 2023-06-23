from tkinter import *

food = ['pizza','hamburger','hotdog']
window = Tk()
x = IntVar()

def order():
    if(x.get()==0):
        print("You ordered pizza.")
    elif(x.get()==1):
        print("You ordered hamburger.")
    else:
        print("You ordered hotdog.")

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text = food[index],
                              variable = x,value = index,
                              padx=25,
                              font = ("Impact",50),
                              command =order #set command of radiobutton to function
                              )
    radiobutton.pack(anchor=W)
window.mainloop()