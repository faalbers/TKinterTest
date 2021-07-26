import tkinter as TK

root = TK.Tk()
root.title('Image example')

frame = TK.LabelFrame(root, text='My Frame', padx=100, pady=100)
frame.pack(padx=50, pady=50)

button = TK.Button(frame, text='CLICK!', command=root.quit).pack()

root.mainloop()
