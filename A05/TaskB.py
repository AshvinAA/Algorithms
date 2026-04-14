from collections import deque

import sys 

input,output= sys.stdin.readline , sys.stdout.write

nodes, edges=map(int, input().split())

graph = [[] for _ in range(nodes+1)]

u=list(map(int, input().split()))
v=list(map(int, input().split()))

for i in range(edges):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])


visited = [ False for _ in range(nodes+1) ]


start_Node = 1

queue = deque()

queue.append(start_Node)

visited[start_Node] = True

out=[]

while(len(queue)!=0):
    node = queue.pop()

    out.append(node)

    for edge in graph[node]:
        if(visited[edge] == False):
            visited[edge] = True
            queue.append(edge)

output(" ".join(map(str,out)))











