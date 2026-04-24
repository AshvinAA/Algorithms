#Locksmith 

import sys
from collections import deque

input = sys.stdin.readline

def solve():
    line = input().split()
    S = line[0]
    C = line[1]
    
    n = int(input())
    forbidden = set()
    for _ in range(n):
        forbidden.add(input().strip())
    
    if C in forbidden:
        print(-1)
        return
    
    if S == C:
        print(0)
        return
    
    queue = deque()
    queue.append((S, 0))
    visited = set()
    visited.add(S)
    
    while queue:
        combo, steps = queue.popleft()
        
        for i in range(4):
            d = int(combo[i])
            for delta in (1, -1):
                new_d = (d + delta) % 10
                new_combo = combo[:i] + str(new_d) + combo[i+1:]
                
                if new_combo == C:
                    print(steps + 1)
                    return
                
                if new_combo not in forbidden and new_combo not in visited:
                    visited.add(new_combo)
                    queue.append((new_combo, steps + 1))
    
    print(-1)

solve()