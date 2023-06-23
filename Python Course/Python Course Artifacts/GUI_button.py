from tkinter import *
def click():
    print("you clicked the button!")
window = Tk()
button = Button(window,
                text = "click me",
                command = click,
                font = ("Comic Sans",30),
                fg ="#00FF00",
                bg = 'black',
                activeforeground='#00FF00',
                activebackground='black')
button.pack()
window.mainloop()