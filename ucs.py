def  uniform_cost_search(goal, start):   
    global graph,cost
    reply = []  
    queue = []
  
    for i in range(len(goal)):
        reply.append(10**8)
  
    queue.append([0, start])
  
    visited = {}
 
    count = 0
 
    while (len(queue) > 0):
 
        queue = sorted(queue)
        p = queue[-1]
 
        del queue[-1]
 
        p[0] *= -1
 
        if (p[1] in goal):
 
            index = goal.index(p[1])
 
            if (reply[index] == 10**8):
                count += 1
 
            if (reply[index] > p[0]):
                reply[index] = p[0]
 
            del queue[-1]
 
            queue = sorted(queue)
            if (count == len(goal)):
                return reply
 
        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):
 
                queue.append( [(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])
 
        visited[p[1]] = 1
 
    return reply
