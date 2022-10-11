# import required modules
import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
  
  
  
# adjust window
root=tk.Tk()
root.geometry("500x500")
  
# loading the images
picture1=ImageTk.PhotoImage(Image.open("p2.jpg"))
picture2=ImageTk.PhotoImage(Image.open("p3.jpg"))
picture3=ImageTk.PhotoImage(Image.open("p4.jpg"))
  
b=Label()
b.pack()
  
  
  
# using recursion to slide to next image
i = 1
  
# function to change to slide image
def move():
    global i
    if i == 4:
        i = 1
    if i == 1:
        b.config(image=picture1)
    elif i == 2:
        b.config(image=picture2)
    elif i == 3:
        b.config(image=picture3)
    i = i+1
    root.after(2000, move)
  
# calling the function
move()
root.mainloop()