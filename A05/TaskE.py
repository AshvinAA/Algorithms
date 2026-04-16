#Reachability

from collections import deque

import sys 
sys.setrecursionlimit(2*100000+5)

input,output= sys.stdin.readline , sys.stdout.write

nodes,edges,queries=map(int, input().split())

graph = [[] for _ in range(nodes+1)]

if edges>0:
    for i in range(edges):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)


def is_Reachable(source, destination):
    if source == destination:
        return True

    visited = [False for _ in range(nodes + 1)]


    queue = deque()

    visited[source]=True

    queue.append(source)

    while(len(queue) != 0):
        current = queue.popleft()

        if current == destination:
            return True
        
        for neighbour in graph[current]:
            if(visited[neighbour] == False):
                visited[neighbour] = True
                queue.append(neighbour)

    return visited[destination]

out=[]

for _ in range(queries):
    source,destination=map(int, input().split())
    if(is_Reachable(source, destination)==True):
        out.append("YES")
    else:
        out.append("NO")


output("\n".join(map(str,out)) + "\n")
