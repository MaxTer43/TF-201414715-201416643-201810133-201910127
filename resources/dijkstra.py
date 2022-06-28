import math
import heapq as hq

def dijkstra(G, s):
  n = len(G)
  visited = [False]*n
  path = [-1]*n
  cost = [math.inf]*n
  cost[s] = 0
  pqueue = [(0, s)]
  while pqueue:
    g, u = hq.heappop(pqueue)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        if not visited[v]:
          f = g + w
          if f < cost[v]:
            cost[v] = f
            path[v] = u
            hq.heappush(pqueue, (f, v))

  return path


def dijkstra_tf(G, start, meta):
  path = dijkstra(G, start)

  rpta = [-1]*len(G)
  while meta != start:
    rpta[meta] = path[meta]
    meta = path[meta]
    if meta == -1:
      rpta = -1
      break

  return rpta