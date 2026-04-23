#Maximum Distance from a Node in a Tree

import sys
from collections import deque

input, output = sys.stdin.readline, sys.stdout.write

nodes = int(input())
edges = nodes - 1

graph = [[] for _ in range(nodes + 1)]

for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(source):
    distance = [-1 for _ in range(nodes + 1)]
    
    queue = deque([source])
    distance[source] = 0
    
    farthest_node = source
    max_dist = 0

    while len(queue) != 0:
        current = queue.popleft()
        
        if distance[current] > max_dist:
            max_dist = distance[current]
            farthest_node = current
            
        for neighbour in graph[current]:
            if distance[neighbour] == -1:
                distance[neighbour] = distance[current] + 1
                queue.append(neighbour)
                
    return farthest_node, max_dist


max_u, _ = bfs(1)

max_v, final_max_dist = bfs(max_u)

output(str(final_max_dist) + "\n")
output(str(max_u) + " " + str(max_v) + "\n")