#Shortest Distance and Path that passes through K

from collections import deque
import sys 
sys.setrecursionlimit(2*100000+5)

input,output= sys.stdin.readline , sys.stdout.write

nodes, edges , source, destination , mandatory=map(int, input().split())

graph = [[] for _ in range(nodes+1)]

if edges>0:
    for i in range(edges):
        u,v = map(int, input().split())
        graph[u].append(v)

visited = [False for _ in range(nodes + 1)]
parent = [-1 for _ in range(nodes + 1)]

queue = deque()
visited[source]=True
queue.append(source)

while(len(queue) != 0):
    current = queue.popleft()
    
    if(current == mandatory):
        break

    for neighbour in graph[current]:
        if(visited[neighbour] == False):
            parent[neighbour] = current
            visited[neighbour] = True
            queue.append(neighbour)

def path_finder(path, target, start_node):
    if(parent[target] == -1):
        if(target == start_node):
            return [start_node], 0
        return None, -1

    step = target
    while(step!=-1):
        path.append(step)
        step = parent[step]
        
    path.reverse()
    return path, len(path)-1 

path1 = path_finder([], mandatory, source)

visited = [False for _ in range(nodes + 1)]
parent = [-1 for _ in range(nodes + 1)]
queue = deque()

visited[mandatory]=True
queue.append(mandatory)

while(len(queue) != 0):
    current = queue.popleft()
    
    if(current == destination):
        break

    for neighbour in graph[current]:
        if(visited[neighbour] == False):
            parent[neighbour] = current
            visited[neighbour] = True
            queue.append(neighbour)

path2 = path_finder([], destination, mandatory)


if(path1[0] == None or path2[0] == None):
    output("-1\n")
else:
    final_path = path1[0][:-1] + path2[0]
    final_dist = path1[1] + path2[1]
    
    output(str(final_dist) + "\n")
    output(" ".join(map(str, final_path)) + "\n")


    
    