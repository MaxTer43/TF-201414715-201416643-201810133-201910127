class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def minimumDistance(self, distance, shortestPathTreeSet):
        min = 1e7
 
        for v in range(self.V):
            if distance[v] < min and searchPathTreeSet[v] == False:
                min = distance[v]
                minimum_index = v
 
        return minimum_index

    def dijkstra(self, source):
        distance = [1e7] * self.V
        distance[source] = 0
        shortestPathTreeSet = [False] * self.V
 
        for cout in range(self.V):
            u = self.minimumDistance(distance, shortestPathTreeSet)
            shortestPathTreeSet[u] = True
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   shortestPathTreeSet[v] == False and
                   distance[v] > distance[u] + self.graph[u][v]):
                    distance[v] = distance[u] + self.graph[u][v]