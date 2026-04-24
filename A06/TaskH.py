#Lexicographical order of characters based on given words
import sys
import heapq
from collections import defaultdict

input, output = sys.stdin.readline, sys.stdout.write


N = int(input())
words = [input().strip() for _ in range(N)]

graph = defaultdict(set)
indegree = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
used = set()

# mark used characters
for w in words:
    for ch in w:
        used.add(ch)

# build graph
for i in range(N - 1):
    w1, w2 = words[i], words[i + 1]
    min_len = min(len(w1), len(w2))
    found = False

    for j in range(min_len):
        if w1[j] != w2[j]:
            if w2[j] not in graph[w1[j]]:
                graph[w1[j]].add(w2[j])
                indegree[w2[j]] += 1
            found = True
            break

    # prefix violation
    if not found and len(w1) > len(w2):
        print(-1)
        exit()

# topological sort (lexicographically smallest)
heap = []
for ch in used:
    if indegree[ch] == 0:
        heapq.heappush(heap, ch)

order = []

while heap:
    u = heapq.heappop(heap)
    order.append(u)
    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            heapq.heappush(heap, v)

# cycle check
if len(order) != len(used):
    output("-1\n")
else:
    output("".join(order) + "\n")