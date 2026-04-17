#Cycle Detection

import sys 


sys.setrecursionlimit(300000)

input, output = sys.stdin.readline, sys.stdout.write

nodes, edges = map(int, input().split())

graph = [[] for _ in range(nodes + 1)]

for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)


visited = [0 for _ in range(nodes + 1)]

def is_Cycle(current):
    
    visited[current] = 1 

    for neighbour in graph[current]:
        if visited[neighbour] == 1:
            
            return True
        elif visited[neighbour] == 0:
            
            if is_Cycle(neighbour):
                return True
                
    visited[current] = 2 
    return False

def solve():
   
    for i in range(1, nodes + 1):
        if visited[i] == 0:
            if is_Cycle(i):
                output("YES\n")
                return
                
    output("NO\n")

solve()