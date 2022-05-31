import dijkstra
import datetime

if __name__=='__main__':
    time = datetime.datetime.now()
    hour = time.strftime("%H")

    print("Waze en progreso")
    
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