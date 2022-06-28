from tkinter import *
from time import strftime
from PIL import Image, ImageTk

import resources.uwu as uwu

def time():
    string = strftime('%H:%M')
    l3.config(text = string)
    l3.after(1, time)

def updateImage():
   image=Image.open('image/graphTF.gv.png')
   img2=image.resize((780, 580))
   img = ImageTk.PhotoImage(img2)
   lblImage.configure(image=img)
   lblImage.image = img

def drawGraph():
    inp1 = inputtxt1.get(1.0, "end-1c")
    inp2 = inputtxt2.get(1.0, "end-1c")
    uwu.draw_graphTf(int(inp1), int(inp2)) #List de adyacencia.
    updateImage()

def flip():
    inp1 = inputtxt1.get(1.0, "end-1c")
    inp2 = inputtxt2.get(1.0, "end-1c")

if __name__=='__main__':
    root = Tk()
    root.geometry("980x720")
    root.title("Mapa uwu")

    image=Image.open('image/graphTF.gv.png')
    img2=image.resize((760, 560))
    img = ImageTk.PhotoImage(img2)
    lblImage = Label(root, image = img)
    lblImage.pack(fill='both', expand=True)

    l3 = Label(root)
    l3.pack()

    inputtxt1 = Text(root, height = 1, width = 80, bg = "light yellow")
    inputtxt1.pack()
    inputtxt2 = Text(root, height = 1, width = 80, bg = "light blue")
    inputtxt2.pack()

    Flip = Button(root, text = "Invertir", width = 10, height = 2, command=flip)
    Search = Button(root, text = "Buscar", width = 10, height = 1, command=drawGraph)
    Search.pack()

    time()
    root.mainloop()