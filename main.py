print("Bone jaw")

from tkinter import *
import random
import time

from PIL import Image, ImageTk


w = 800
h = 600

root=Tk()
canvas = Canvas(root, width=w, height =h,background='white')
root.title("DVD")
canvas.pack()

pic1 = PhotoImage(file='rsz_dvd_logo.png')
img1  = Image.open('rsz_dvd_logo.png')
tk_pil_img = ImageTk.PhotoImage(img1)

imw = tk_pil_img.width()
imh= tk_pil_img.height()

img = canvas.create_image(60,60, image=pic1)

xspeed= 3
yspeed = 3
while True:
    canvas.move(img,xspeed,yspeed)
    pos = canvas.coords(img) 
    root.update()
    collision=False

    if pos[0] <= 0+imw/2 or pos[0] >= w - imw/2:
        xspeed *= -1
        collision=True

    if pos[1] <= 0+imh/2 or pos[1] >= h - imh/2:
        yspeed *= -1
        collision=True

    time.sleep(0.01)

root.mainloop()