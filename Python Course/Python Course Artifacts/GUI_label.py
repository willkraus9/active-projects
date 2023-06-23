#label = area widget holds text / image within window
from tkinter import *

window = Tk()
#photo = PhotoImage(file='xxx')
label = Label(window,
              text = "Hello world!", 
              font = ('Times New Roman', 40,'italic'), 
              fg = '#00FF00', 
              bg = 'black',
              relief = RAISED,
              bd = 10,
              padx =20,
              pady=20)#image = photo, compound='bottom'
label.pack()
#label.place(x=0,y=0)

window.mainloop()

