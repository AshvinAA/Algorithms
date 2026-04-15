from collections import deque

import sys 
sys.setrecursionlimit(2*100000+5)

input,output= sys.stdin.readline , sys.stdout.write

nodes, edges=map(int, input().split())

graph = [[] for _ in range(nodes+1)]

u=list(map(int, input().split()))
v=list(map(int, input().split()))

for i in range(edges):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])


visited = [ False for _ in range(nodes+1) ]
out=[]

start_Node = 1

def dfs(Graph ,u):
    visited[u] = True
    out.append(u)

    for edges in Graph[u]:
        if visited[edges] == False:
            dfs(Graph , edges)


dfs(graph , start_Node)

output(" ".join(map(str,out)))











