from collections import deque

import sys 
sys.setrecursionlimit(2*100000+5)

input,output= sys.stdin.readline , sys.stdout.write

nodes, edges , source, destination=map(int, input().split())

graph = [[] for _ in range(nodes+1)]

if edges>0:
    u=list(map(int, input().split()))
    v=list(map(int, input().split()))
    
    for i in range(edges):
        graph[u[i]].append(v[i])
        graph[v[i]].append(u[i])

for i in range(1, nodes + 1):
    graph[i].sort()


visited = [False for _ in range(nodes + 1)]
parent = [-1 for _ in range(nodes + 1)]

queue = deque()

visited[source]=True

queue.append(source)

while(len(queue) != 0):
    current = queue.popleft()
    

    if(current == destination):
        break

    for neighbour in graph[current]:
        if(visited[neighbour] == False):
            parent[neighbour] = current
            visited[neighbour] = True
            queue.append(neighbour)

def path_finder(path,destination):
    if(parent[destination] == -1):
        if(destination == source):
            return [source],0
        return None,-1

    step = destination
    while(step!=-1):
        path.append(step)
        step = parent[step]
        
    path.reverse()

    return path,len(path)-1 

path = path_finder([], destination)

if(path[0]==None):
    output(str(path[1]))
else:
    output(str(path[1]) + "\n")
    output(" ".join(map(str,path[0])) + "\n")


        
    
    