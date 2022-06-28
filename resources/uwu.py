import resources.dijkstra as dj
import resources.trafficFactor as tra
import graphviz as gv
import resources.classesT as cl


import resources.dfs as dfs
import resources.bfs as bfs

intersections = list()
with open("data/Lima-intersecciones.csv", "r", -1, "utf-8-sig") as files:
  for line in files:
    data = line.split(';')
    intersection = cl.Intersection(data[0], data[1], data[2], data[3], data[4], int(data[5]), int(data[6]), data[7], data[8], int(data[9]), data[10], float(data[11]), float(data[12]), float(data[13]), float(data[14].strip()))
    intersections.append(intersection)

qVertices = []
for x in intersections:
  if ~(x._OrAndDest[0] in qVertices):
    qVertices.append(x._OrAndDest[0])
  elif ~(x._OrAndDest[1] in qVertices):
    qVertices.append(x._OrAndDest[1])

maxL = max(qVertices) + 1

#armar la list de adyacencia
listAd = list()


def updateTraffic():
  sizeI = len(intersections)
  for x in range(sizeI):
     intersections[x]._price = intersections[x]._price * tra.traffic_criteria()


def generateList():
  updateTraffic()
  for x in range(maxL):
    listAd.append(list())

  maxI = len(intersections)
  for x in range(maxI):
    index = intersections[x]._OrAndDest[0]
    listAd[index].append((intersections[x]._OrAndDest[1], intersections[x]._price))
    listAd[index].append((intersections[x]._OrAndDest[1], intersections[x]._price))



def drawG_al(G,  directed=False, weighted=True, path1=[], path2=[], path3=[], layout="dot"):
  graph = gv.Digraph("graphTF")
  graph.graph_attr["layout"] = layout
  graph.edge_attr["color"] = "gray"
  graph.node_attr["color"] = "orangered"
  graph.node_attr["width"] = "0.1"
  graph.node_attr["height"] = "0.1"
  graph.node_attr["fontsize"] = "18"
  graph.node_attr["fontcolor"] = "mediumslateblue"
  graph.node_attr["fontname"] = "monospace"
  graph.edge_attr["fontsize"] = "18"
  graph.edge_attr["fontname"] = "monospace"
  n = len(G)
  added1 = set()
  added2 = set()
  added3 = set()

  for v, u in enumerate(path1):
    if u != -1:
      if weighted:
        for vi, w in G[u]:
          if vi == v:
            break
        graph.edge(str(u), str(v), str(w), dir="forward", penwidth="2", color="green")
      else:
        graph.edge(str(u), str(v), dir="forward", penwidth="2", color="green")
      added1.add(f"{u},{v}")
      added1.add(f"{v},{u}")

  for u in range(n):
    for v, w in G[u]:
      draw = False
      if not directed and not f"{u},{v}" in added1:  
        added1.add(f"{u},{v}")
        added1.add(f"{v},{u}")
        draw = True
      elif directed:
        draw = True
      if draw:
        if weighted:
          graph.edge(str(u), str(v), str(w))
        else:
          graph.edge(str(u), str(v))

  for v, u in enumerate(path2):
    if u != -1:
      if weighted:
        for vi, w in G[u]:
          if vi == v:
            break
        graph.edge(str(u), str(v), str(w), dir="forward", penwidth="2", color="blue")
      else:
        graph.edge(str(u), str(v), dir="forward", penwidth="2", color="blue")
      added2.add(f"{u},{v}")
      added2.add(f"{v},{u}")
  
  for u in range(n):
    for v, w in G[u]:
      draw2 = False
      if not directed and not f"{u},{v}" in added3:  
        added3.add(f"{u},{v}")
        added3.add(f"{v},{u}")
        draw2 = True
      elif directed:
        draw2 = True
      if draw2:
        if weighted:
          graph.edge(str(u), str(v), str(w))
        else:
          graph.edge(str(u), str(v))

  for v, u in enumerate(path3):
    if u != -1:
      if weighted:
        for vi, w in G[u]:
          if vi == v:
            break
        graph.edge(str(u), str(v), str(w), dir="forward", penwidth="2", color="red")
      else:
        graph.edge(str(u), str(v), dir="forward", penwidth="2", color="red")
      added3.add(f"{u},{v}")
      added3.add(f"{v},{u}")
  
  for u in range(n):
    for v, w in G[u]:
      draw2 = False
      if not directed and not f"{u},{v}" in added2:  
        added2.add(f"{u},{v}")
        added2.add(f"{v},{u}")
        draw2 = True
      elif directed:
        draw2 = True
      if draw2:
        if weighted:
          graph.edge(str(u), str(v), str(w))
        else:
          graph.edge(str(u), str(v))

  return graph

def draw_graphTf(start, meta):
  generateList()
  path1 =  dj.dijkstra_tf(listAd, start, meta)
  path2 =  dfs.dfs_tf(listAd, start, meta)
  path3 =  bfs.bfs_tf(listAd, start, meta)

  if path1 == -1: 
    print("No hay camino")
  else: 
    graphTF = drawG_al(listAd, directed=False, weighted=True, path1=path1, path2=path2, path3=path3)
    graphTF.format = 'png'
    graphTF.render(directory="image")