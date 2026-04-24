##Knight's shortest path on a chessboard 

import sys
from collections import deque

output = sys.stdout.write

def solve():
    data = sys.stdin.read().split()
    

    N = int(data[0])
    x1, y1 = int(data[1]), int(data[2])
    x2, y2 = int(data[3]), int(data[4])
    
  
    sx, sy = x1 - 1, y1 - 1
    tx, ty = x2 - 1, y2 - 1

   
    if sx == tx and sy == ty:
        output("0\n")
        return

    
    start_node = sx * N + sy
    target_node = tx * N + ty
    
  
    visited = [0] * (N * N)
    
    visited[start_node] = 1       
    visited[target_node] = -1     

    
    q_fwd = deque([start_node])
    q_bwd = deque([target_node])

    
    moves = [
        (1, 2), (1, -2), (-1, 2), (-1, -2),
        (2, 1), (2, -1), (-2, 1), (-2, -1)
    ]

    while q_fwd and q_bwd:
        if len(q_fwd) <= len(q_bwd):
            current_q = q_fwd
            direction = 1 
        else:
            current_q = q_bwd
            direction = -1 
        
        curr = current_q.popleft()
        curr_val = visited[curr]
        
        curr_dist = abs(curr_val) - 1
        
        cx, cy = divmod(curr, N)
        
        for dx, dy in moves:
            nx, ny = cx + dx, cy + dy
            
            if 0 <= nx < N and 0 <= ny < N:
                neighbor = nx * N + ny
                neighbor_val = visited[neighbor]
                
                if neighbor_val == 0:
                    if direction == 1:
                        visited[neighbor] = curr_val + 1
                    else:
                        visited[neighbor] = curr_val - 1
                    current_q.append(neighbor)
                
                elif (direction == 1 and neighbor_val < 0) or (direction == -1 and neighbor_val > 0):
                    
                    other_dist = abs(neighbor_val) - 1
                    output(f"{curr_dist + 1 + other_dist}\n")
                    return

    output("-1\n")

if __name__ == '__main__':
    solve()