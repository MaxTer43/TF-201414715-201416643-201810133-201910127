import datetime
import dijkstra
from tkinter import * 

if __name__=='__main__':
    root = Tk()
    root.geometry("800x600")
    root.title("Mapa")

    map = Canvas(root, width = 800,
                        height = 450,
                        background = "black")

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

    #Definir arreglos
    intersections = []

    registry_id = []
    street_id = []
    street_name = []
    origin_id = []
    destiny_id = []
    intersection_origin_id = []
    intersection_destiny_id = []
    distance = []
    speed = []
    cost1 = []
    cost2 = []
    x1 = []
    y1 = []
    x2 = []
    y2 = []

    menorX = 0
    menorY = 0
    mayorX = 0
    mayorY = 0
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
            x1.append(intersection[11])
            y1.append(intersection[12])
            x2.append(intersection[13])
            y2.append(intersection[14])

            #print(intersection)
            #print(intersections[i])
            
            #map.create_oval(float(x1[i])+78, float(y1[i])+13, float(x1[i])+10+78, float(y1[i])+10+13, outline='#1375BE')
            #map.create_oval(float(x2[i])+78, float(y2[i])+13, float(x2[i])+10+78, float(y2[i])+10+13, outline='#1375BE')

            #map.create_line(float(x1[i])+5+78, float(y1[i])+5+13, float(x2[i])+5+78, float(y2[i])+5+13, fill="#1375BE", width=100)
            
            #if (i == 0):
            #    map.create_oval(float(x1[i]), float(y1[i]), float(0)+10, float(0)+10, outline='#1375BE')
            if (i == 0):
                menorX = x2[i]
                menorY = y2[i]
                mayorX = x1[i]
                mayorY = y1[i]
            else:
                if (menorX < x1[i]):
                    menorX = x1[i]
                if (menorY < y1[i]):
                    menorY = y1[i]
                if (menorX < x2[i]):
                    menorX = x2[i]
                if (menorY < y2[i]):
                    menorY = y2[i]
                
                if (mayorX > x1[i]):
                    mayorX = x1[i]
                if (mayorY > y1[i]):
                    mayorY = y1[i]
                if (mayorX > x2[i]):
                    mayorX = x2[i]
                if (mayorY > y2[i]):
                    mayorY = y2[i]

            i+=1

    #print(str(x1) + "," + str(y1))

    #print("Coordenadas: " + x1[0] + ";" + y1[0])
    
    print("X menor: " + menorX)
    print("X mayor: " + mayorX)
    print("Y menor: " + menorY)
    print("Y mayor: " + mayorY)

    time = datetime.datetime.now()
    hour = time.strftime("%H")
    min = time.strftime("%M")

    #Lectura de datos
    #print("Calles")
    
    #print("Intersecciones")
    
    #streets()
    #intersections()

    #print("Hora actual: " + hour + ":" + min);
    #print("Waze en progreso")

    #Interfaz

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

    l1.grid(row = 0, column = 0)
    l2.grid(row = 1, column = 0)
    l3.place(x = 350, y = 565)

    inputtxt1.grid(row = 0, column = 1)
    inputtxt2.grid(row = 1, column = 1)

    Flip.grid(row = 0, column = 2)
    Search.grid(row = 1, column = 2)

    

    map.place(x = -1, y = 100)

    #i = 0

    #La cantidad total de líneas en el archivo de intersecciones es 84673
    #for i in range(84673):
    #    intersection = [item.strip() for item in i.split(';')]
    #    map.create_oval(10, 10, intersection[13], intersection[14], outline='#1375BE')
    

    
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