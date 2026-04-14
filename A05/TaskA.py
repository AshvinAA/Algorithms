from collections import deque

import sys 

input,output= sys.stdin.readline , sys.stdout.write

nodes, edges=map(int, input().split())

graph = [[] for _ in range(nodes+1)]

for _ in range(edges):
    node1, node2=map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)


visited = [ False for _ in range(nodes+1) ]


start_Node = 1

queue = deque()

queue.append(start_Node)

visited[start_Node] = True

out=[]

while(len(queue)!=0):
    node = queue.popleft()

    out.append(node)

    for edge in graph[node]:
        if(visited[edge] == False):
            visited[edge] = True
            queue.append(edge)

output(" ".join(map(str,out)))











