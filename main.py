import datetime
import dijkstra
from tkinter import *

def streets():
    #Definir arreglos
    streets = []

    street_id = []
    street_name = []
    intersections_amount = []

    #Lectura de archivo de texto
    with open ("Lima-calles.csv") as textFile:
        for line in textFile:
            street = [item.strip() for item in line.split(';')]
            streets.append(street)

            street_id.append(street[0])
            street_name.append(street[1])
            intersections_amount.append(street[2])
            #print(street)
    #print(streets)

def intersections():
    #Definir arreglos
    intersections = []

    registry_id = []
    street_id = []
    street_name = []
    origin_id = destiny_id = []
    intersection_origin_id = intersection_destiny_id = []
    distance = []
    speed = []
    cost1 = []
    cost2 = []
    y1 = x1 = []
    y2 = x2 = []

    #Lectura de archivo de texto
    with open ("Lima-intersecciones.csv") as textFile:
        i = 0
        for line in textFile:
            intersection = [item.strip() for item in line.split(';')]
            intersections.append(intersection)

            registry_id.append(intersection[0])
            street_id.append(intersection[1])
            street_name.append(intersection[2])

            origin_id.append(intersection[3])
            destiny_id.append(intersection[4])

            intersection_origin_id.append(intersection[5])
            intersection_destiny_id.append(intersection[6])

            distance.append(intersection[7])
            speed.append(intersection[8])
            cost1.append(intersection[9])
            cost2.append(intersection[10])
            y1.append(intersection[11])
            x1.append(intersection[12])
            y2.append(intersection[13])
            x2.append(intersection[14])
            #print(intersection)
            #print(intersections[i])
            i+=1

if __name__=='__main__':
    time = datetime.datetime.now()
    hour = time.strftime("%H")
    min = time.strftime("%M")

    #Lectura de datos
    #print("Calles")
    
    #print("Intersecciones")
    
    streets()
    intersections()
    #print("Hora actual: " + hour + ":" + min);
    #print("Waze en progreso")

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

    i = 0

    #La cantidad total de líneas en el archivo de intersecciones es 84673
    #for i in range(84673):
    #    intersection = [item.strip() for item in i.split(';')]
    #    map.create_oval(10, 10, intersection[13], intersection[14], outline='#1375BE')
    

    map.create_oval(50,50,200,20, outline='#1375BE')
    #map.create_line(35,35, 150, 150, fill="#1375BE", width=1)

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