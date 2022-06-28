def bfs_al(G, s):
  n = len(G)
  visited = [False]*n
  path = [-1]*n # parent
  queue = [s]
  visited[s] = True

  while queue:
    u = queue.pop(0)
    for v,_ in G[u]:
      if not visited[v]:
        visited[v] = True
        path[v] = u
        queue.append(v)

  return path

def bfs_tf(G, start, meta):
  path = bfs_al(G, start)

  rpta = [-1]*len(G)
  while meta != start:
    rpta[meta] = path[meta]
    meta = path[meta]
    if meta == -1:
      rpta = -1
      break

  return rpta