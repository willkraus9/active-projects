from tkinter import *

def submit():
    print("The temperature is: "+str(scale.get())+ " degrees C")
window = Tk()

scale = Scale(window,
              from_=100, to=0,
              tickinterval =10,
              showvalue = 1 #0 would hide current value
)

button = Button(window,
                text="submit",
                command = submit)
button.pack()
scale.pack()
window.mainloop()