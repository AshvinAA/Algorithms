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

visited_by = [-1 for _ in range(nodes + 1)]

def is_Reachable(source, destination):
   
    if visited_by[source] == -1:
        
        queue = deque()
        
        visited_by[source] = source 
        queue.append(source)

        while(len(queue) != 0):
            current = queue.popleft()
            
            for neighbour in graph[current]:
                if(visited_by[neighbour] == -1):
                    
                    visited_by[neighbour] = source
                    queue.append(neighbour)

    
    return visited_by[source] == visited_by[destination]

out=[]

for _ in range(queries):
    source,destination=map(int, input().split())
    if(is_Reachable(source, destination)==True):
        out.append("YES")
    else:
        out.append("NO")

output("\n".join(map(str,out)) + "\n")