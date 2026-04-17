#Maze puzzle

import sys
from collections import deque

input_data = sys.stdin.read().split()

if input_data:
    R = int(input_data[0])
    H = int(input_data[1])
    grid = input_data[2:] 
    
    visited = [[False for _ in range(H)] for _ in range(R)]
    
    max_diamonds = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for r in range(R):
        for c in range(H):
            if grid[r][c] != '#' and not visited[r][c]:
                
                current_island_diamonds = 0
                queue = deque([(r, c)])
                visited[r][c] = True
                
                while len(queue) != 0:
                    curr_r, curr_c = queue.popleft()
                    
                    if grid[curr_r][curr_c] == 'D':
                        current_island_diamonds += 1
                        
                    for dr, dc in directions:
                        new_r = curr_r + dr
                        new_c = curr_c + dc
                        
                        if 0 <= new_r < R and 0 <= new_c < H:
                            if grid[new_r][new_c] != '#' and not visited[new_r][new_c]:
                                visited[new_r][new_c] = True
                                queue.append((new_r, new_c))
                                
                if current_island_diamonds > max_diamonds:
                    max_diamonds = current_island_diamonds
                    
    print(max_diamonds)