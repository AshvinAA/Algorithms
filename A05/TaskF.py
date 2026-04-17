#SubTree Size

from collections import defaultdict, deque

def calculate_subtree_sizes(n, r, graph):
    
    parent = [-1] * (n + 1)
    children = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    queue = deque([r])
    visited[r] = True
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                children[node].append(neighbor)
                queue.append(neighbor)
    
    subtree_size = [0] * (n + 1)
    stack = [(r, False)]  
    
    while stack:
        node, processed = stack.pop()
        
        if processed:
            subtree_size[node] = 1
            for child in children[node]:
                subtree_size[node] += subtree_size[child]
        else:
            stack.append((node, True))
            for child in children[node]:
                stack.append((child, False))
    
    return subtree_size


  
n, r = map(int, input().split())

graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

subtree_size = calculate_subtree_sizes(n, r, graph)

q = int(input())
for _ in range(q):
    x = int(input())
    print(subtree_size[x])

