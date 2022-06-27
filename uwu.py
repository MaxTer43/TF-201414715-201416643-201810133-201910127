import resources.classes as cl
import graphviz as gv
import resources.dijkstra as dj
intersections = list()
with open("data/Lima-intersecciones.csv", "r", -1, "utf-8-sig") as files:
  for line in files:
    data = line.split(';')
    intersection = cl.Intersection(data[0], data[1], data[2], data[3], data[4], int(data[5]), int(data[6]), data[7], data[8], float(data[9]), data[10], float(data[11]), float(data[12]), float(data[13]), float(data[14].strip()))
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

for x in range(maxL):
  listAd.append(list())

maxI = len(intersections)
for x in range(maxI):
  index = intersections[x]._OrAndDest[0]
  listAd[index].append((intersections[x]._OrAndDest[1], intersections[x]._price))
  listAd[index].append((intersections[x]._OrAndDest[1], intersections[x]._price))



def drawG_al(G, directed=False, weighted=False, path=[], layout="sfdp"):
  graph = gv.Digraph("graphTF")
  graph.graph_attr["layout"] = layout
  graph.edge_attr["color"] = "gray"
  graph.node_attr["color"] = "orangered"
  graph.node_attr["width"] = "0.1"
  graph.node_attr["height"] = "0.1"
  graph.node_attr["fontsize"] = "8"
  graph.node_attr["fontcolor"] = "mediumslateblue"
  graph.node_attr["fontname"] = "monospace"
  graph.edge_attr["fontsize"] = "8"
  graph.edge_attr["fontname"] = "monospace"
  n = len(G)
  added = set()
  for v, u in enumerate(path):
    if u != -1:
      if weighted:
        for vi, w in G[u]:
          if vi == v:
            break
        graph.edge(str(u), str(v), str(w), dir="forward", penwidth="2", color="orange")
      else:
        graph.edge(str(u), str(v), dir="forward", penwidth="2", color="orange")
      added.add(f"{u},{v}")
      added.add(f"{v},{u}")
  for u in range(n):
    for v, w in G[u]:
      draw = False
      if not directed and not f"{u},{v}" in added:  
        added.add(f"{u},{v}")
        added.add(f"{v},{u}")
        draw = True
      elif directed:
        draw = True
      if draw:
        if weighted:
          graph.edge(str(u), str(v), str(w))
        else:
          graph.edge(str(u), str(v))
  return graph


def draw_graphTf(start, meta):
  path =  dj.dijkstra(listAd, start, meta)

  if path == -1: 
    print("No hay camino")
  else: 
    graphTF = drawG_al(listAd, directed=False, weighted=False, path=path)
    graphTF.format = 'png'
    graphTF.render(directory="image", view=True)