import dijkstra
from tkinter import *

#Obtener hora del sistema
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    l3.config(text = string)
    l3.after(1000, time)

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

            distance.append(float(intersection[7]))
            speed.append(float(intersection[8]))
            cost1.append(float(intersection[9]))
            cost2.append(float(intersection[10]))
            x1.append(float(intersection[11]))
            y1.append(float(intersection[12]))
            x2.append(float(intersection[13]))
            y2.append(float(intersection[14]))

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
                if (menorX > x1[i]):
                    menorX = x1[i]
                if (menorY > y1[i]):
                    menorY = y1[i]
                if (menorX > x2[i]):
                    menorX = x2[i]
                if (menorY > y2[i]):
                    menorY = y2[i]
                
                if (mayorX < x1[i]):
                    mayorX = x1[i]
                if (mayorY < y1[i]):
                    mayorY = y1[i]
                if (mayorX < x2[i]):
                    mayorX = x2[i]
                if (mayorY < y2[i]):
                    mayorY = y2[i]

            i+=1

    #print(str(x1) + "," + str(y1))

    #print("Coordenadas: " + x1[0] + ";" + y1[0])
    
    print("X menor: " + str(menorX))
    print("X mayor: " + str(mayorX))
    print("Y menor: " + str(menorY))
    print("Y mayor: " + str(mayorY))
    distanciaX = menorX-mayorX
    distanciaY = menorY-mayorY
    print("Distancia X: " + str(distanciaX))
    print("Distancia Y: " + str(distanciaY))
    ancho = distanciaX*950
    largo = distanciaY*950
    print(str(ancho))
    print(str(largo))
    print("Total X: " + str((x1[0]-menorX)))

    xr1 = []
    yr1 = []
    xr2 = []
    yr2 = []

    scale = 880
    j = 0
    for j in range(i):
        map.create_oval((x1[j]-menorX)*scale, (y1[j]-menorY)*scale, (x1[j]-menorX)*scale+10, (y1[j]-menorY)*scale+10, outline='#1375BE')
        map.create_oval((x2[j]-menorX)*scale, (y2[j]-menorY)*scale, (x2[j]-menorX)*scale+10, (y2[j]-menorY)*scale+10, outline='#1375BE')
        map.create_line((x1[j]-menorX)*scale+5, (y1[j]-menorY)*scale+5, (x2[j]-menorX)*scale+5, (y2[j]-menorY)*scale+5, fill="#1375BE", width=1)

    #Interfaz

    Flip = Button(root, text = "Invertir", width = 10, height = 2)
    Search = Button(root, text = "Buscar", width = 10, height = 2)

    l1 = Label(text = "Inicio")
    l2 = Label(text = "Final")
    l3 = Label(root)

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
    time()
    root.mainloop()