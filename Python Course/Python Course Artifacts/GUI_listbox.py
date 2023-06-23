#listbox = listing of selectable text items (buttons) within container

from tkinter import *

def submit():
    print(listbox.get(listbox.curselection()))
window = Tk()
listbox = Listbox(window,
                  bg='#f7ffde',
                  font = ('Constantia',35),
                  width = 12)

#listbox.place(anchor=N) #puts in northernmost list
listbox.pack()

listbox.insert(1,'pizza')
listbox.insert(2,'pasta')
listbox.insert(3,'garlic bread')
listbox.insert(4,'soup')
listbox.insert(5,'salad')

#change size of list box
listbox.config(height = listbox.size())
submitButton = Button(window, text = "Submit",command = submit)
submitButton.pack()

window.mainloop()