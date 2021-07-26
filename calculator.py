from tkinter import Tk, Entry, Button, END

root = Tk()
root.title('Simple Calculator')
root.iconbitmap('calc.ico')

entry = Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def click(char):
    entry.insert(END, char)

def clear():
    entry.delete(0, END)

def equals():
    result = eval(entry.get())
    entry.delete(0, END)
    entry.insert(0, str(result))

for y in range(0, 3):
    for x in range(0, 3):
        butnum = x+3*(2-y)+1
        myButton = Button(root, text=str(butnum),
            width=10,
            borderwidth=5,
            command=lambda butnum=butnum: click(str(butnum)))
        myButton.grid(row=y+1, column=x)      

myButton = Button(root, text='0',
            width=10,
            borderwidth=5,
            command=lambda: click('0'))
myButton.grid(row=4, column=0)

myButton = Button(root, text='Clear',
            width=23,
            borderwidth=5,
            command=clear)
myButton.grid(row=4, column=1, columnspan=2)

myButton = Button(root, text='+',
            width=10,
            borderwidth=5,
            command=lambda: click('+'))
myButton.grid(row=5, column=0)

myButton = Button(root, text='=',
            width=23,
            borderwidth=5,
            command=equals)
myButton.grid(row=5, column=1, columnspan=2)

myButton = Button(root, text='Exit',
            width=23,
            borderwidth=5,
            command=root.quit)
myButton.grid(row=6, column=0, columnspan=3)

root.mainloop()

