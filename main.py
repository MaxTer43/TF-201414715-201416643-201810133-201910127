from tkinter import *
from time import strftime
import uwu

def time():
    string = strftime('%H:%M')
    l3.config(text = string)
    l3.after(1000, time)

def updateImage():
   img = PhotoImage(file='image/graphTF.gv.png')
   lblImage.configure(image=img)
   lblImage.image = img


def drawGraph():
    inp1 = inputtxt1.get(1.0, "end-1c")
    inp2 = inputtxt2.get(1.0, "end-1c")
    uwu.draw_graphTf(int(inp1), int(inp2))
    updateImage()

if __name__=='__main__':
    root = Tk()
    root.geometry("800x600")
    root.title("Mapa uwu")

    img = PhotoImage(file='image/graphTF.gv.png')
    lblImage = Label(root, image = img).place(x=100, y = 100)


    l1 = Label(text = "Inicio")
    l2 = Label(text = "Final")
    l3 = Label(root)

    inputtxt1 = Text(root, height = 2, width = 80, bg = "light yellow")
    inputtxt2 = Text(root, height = 2, width = 80, bg = "light blue")


    Flip = Button(root, text = "Invertir", width = 10, height = 2)
    Search = Button(root, text = "Buscar", width = 10, height = 2, command=drawGraph)


    l1.grid(row = 0, column = 0)
    l2.grid(row = 1, column = 0)
    l3.place(x = 350, y = 565)

    inputtxt1.grid(row = 0, column = 1)
    inputtxt2.grid(row = 1, column = 1)

    Flip.grid(row = 0, column = 2)
    Search.grid(row = 1, column = 2)
    
    #time()
    root.bind("<Return>", updateImage)
    root.mainloop()
