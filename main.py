import datetime
import dijkstra
import lima
from tkinter import *

if __name__=='__main__':
    time = datetime.datetime.now()
    hour = time.strftime("%H")
    min = time.strftime("%M")

    #Lectura de datos
    print("Calles")
    lima.streets()
    print("Intersecciones")
    lima.intersections()

    print("Hora actual: " + hour + ":" + min);
    print("Waze en progreso")

    #Interfaz

    root = Tk()
    root.geometry("800x600")
    root.title("Mapa")

    Flip = Button(root, text = "Invertir", width = 10, height = 2)
    Search = Button(root, text = "Buscar", width = 10, height = 2)

    l1 = Label(text = "Inicio")
    l2 = Label(text = "Final")
    l3 = Label(text= hour + ":" + min)

    inputtxt1 = Text(root, height = 2,
                width = 80,
                bg = "light yellow")
    inputtxt2 = Text(root, height = 2,
                width = 80,
                bg = "light blue")

    map = Canvas(root, width = 800,
                        height = 450,
                        background = "black")

    l1.grid(row = 0, column = 0)
    l2.grid(row = 1, column = 0)
    l3.place(x = 350, y = 565)

    inputtxt1.grid(row = 0, column = 1)
    inputtxt2.grid(row = 1, column = 1)

    Flip.grid(row = 0, column = 2)
    Search.grid(row = 1, column = 2)

    map.place(x = -1, y = 100)

    root.mainloop()
    
    # g = dijkstra.Graph(9)
    # g.graph = [[2, 2, 1, 8, 6, 2, 1, 0, 9],
    #            [2, 2, 1, 8, 6, 2, 1, 0, 9],
    #            [2, 2, 1, 8, 6, 2, 1, 2, 9],
    #            [2, 2, 1, 8, 6, 2, 1, 0, 9],
    #            [2, 2, 1, 8, 6, 2, 1, 0, 9],
    #            [2, 2, 1, 8, 6, 2, 1, 7, 9],
    #            [2, 2, 1, 8, 6, 2, 1, 0, 9],
    #            [2, 2, 1, 8, 6, 2, 1, 0, 9],
    #            [2, 2, 1, 8, 6, 2, 1, 0, 9]
    #            ]
 
    # g.dijkstra(0)