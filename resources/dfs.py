def dfs_al(G, s):
  print(G)
  n = len(G)
  path = [-1]*n
  visited = [False]*n

  def dfs(u):
    visited[u] = True
    for v,_ in G[u]:
      if not visited[v]:
        path[v] = u
        dfs(v)

  dfs(s)
  return path

def dfs_tf(G, start, meta):
  path = dfs_al(G, start)

  rpta = [-1]*len(G)
  while meta != start:
    rpta[meta] = path[meta]
    meta = path[meta]
    if meta == -1:
      rpta = -1
      break

  return rpta
