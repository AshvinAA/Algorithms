#Topological Course Order

import sys
from collections import deque 


input,output= sys.stdin.readline , sys.stdout.write

n = int(input())

for _ in range(n):

    def solve():
        nodes, edges = map(int, input().split())

        graph = [[] for _ in range(nodes + 1)]

        for _ in range(edges):
            u, v = map(int, input().split())
            graph[u].append(v)

        incoming_edges = [0 for _ in range(nodes + 1)]

        def count_Incoming_Edges(incoming_edges, graph):
            for node in range(1, nodes + 1):
                for neighbour in graph[node]:
                    incoming_edges[neighbour] += 1

        count_Incoming_Edges(incoming_edges, graph)
    
        out = []

        def kahns_Algorithm(graph, incoming_edges):
            queue = deque()

            for node in range(1, nodes + 1):
                if incoming_edges[node] == 0:
                    queue.append(node)

            while len(queue) != 0:
                current = queue.popleft()
                out.append(current)

                for neighbour in graph[current]:
                    incoming_edges[neighbour] -= 1

                    if incoming_edges[neighbour] == 0:
                        queue.append(neighbour)
        kahns_Algorithm(graph, incoming_edges)
        if len(out) != nodes:
            output("-1\n")
        else:
            output(" ".join(map(str, out)) + "\n")
    solve()