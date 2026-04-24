#Nearest Tour Destination

import sys
from collections import deque


input,output= sys.stdin.readline , sys.stdout.write

nodes, edges , source_nodes, destination_nodes = map(int, input().split())

graph = [[] for _ in range(nodes + 1)]

for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

source = list(map(int, input().split()))
destination = list(map(int, input().split()))



def bfs(sources):
    distance = [-1 for _ in range(nodes + 1)]
    queue = deque()
    
    for s in sources:
        distance[s] = 0
        queue.append(s)
    
    while len(queue) != 0:
        current = queue.popleft()
        
        for neighbour in graph[current]:
            if distance[neighbour] == -1:
                distance[neighbour] = distance[current] + 1
                queue.append(neighbour)
                
    return distance

distances = bfs(source)

results = []
for dest in destination:
    results.append(str(distances[dest]))

output(" ".join(results) + "\n")