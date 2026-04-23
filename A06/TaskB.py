#Two Teams 


import sys
from collections import deque


input,output= sys.stdin.readline , sys.stdout.write

nodes, edges = map(int, input().split())

graph = [[] for _ in range(nodes + 1)]

for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

colours = [0 for _ in range(nodes + 1)]
answer = 0

def bfs(start_node):
    queue = deque([start_node])
    colours[start_node] = 1
    human_count = 1
    robot_count = 0

    while queue:
        current = queue.popleft()

        for neighbour in graph[current]:
            if colours[neighbour] == 0:
                colours[neighbour] = -colours[current]
                if colours[neighbour] == 1:
                    human_count += 1
                else:
                    robot_count += 1
                queue.append(neighbour)

    return max(human_count, robot_count)

for node in range(1, nodes + 1):
    if colours[node] == 0:
        if len(graph[node]) == 0:
            answer += 1
        else:
            answer += bfs(node)

output(str(answer) + "\n")
    

