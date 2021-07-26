from tkinter import Tk, Label, Button, PhotoImage, SUNKEN, W, E
from PIL import ImageTk

root = Tk()
root.title('Image example')

my_imgs = []
my_img1 = ImageTk.PhotoImage(file='Image20.jpg')
my_img1.name = 'Image20.jpg'
my_imgs.append(my_img1)
my_img2 = ImageTk.PhotoImage(file='Image19.jpg')
my_img2.name = 'Image19.jpg'
my_imgs.append(my_img2)

def blah():
    global my_label, my_status
    my_label.currentImage += 1
    if my_label.currentImage == len(my_imgs):
        my_label.currentImage = 0
    image = my_imgs[my_label.currentImage]
    my_label.configure(image=image)
    my_status.configure(text=image.name)

my_label = Label(root, image=my_img1)
my_label.currentImage = 0
my_status = Label(root, text=my_imgs[my_label.currentImage].name, relief=SUNKEN)
my_label.grid()
my_status.grid(sticky=W+E)

my_button = Button(root, text='next', command=blah)
my_button .grid(sticky=W+E)

root.mainloop()
