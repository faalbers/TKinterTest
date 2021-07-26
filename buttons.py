from tkinter import *

root = Tk()

myEntry = Entry(root,
    width=50,
    borderwidth=5)
myEntry.insert(0, 'Fill in something')
myEntry.pack()

def myClick():
    myLabel = Label(root, text=myEntry.get()).pack()

Button(root, text='Enter',
    padx=50,
    borderwidth=5,
    command=myClick,
    fg='yellow',
    bg='#ff0000').pack()

root.mainloop()
