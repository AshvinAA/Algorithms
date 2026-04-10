#Co Prime Graph

import sys
import math

def solve():
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    Q = int(input_data[1])
    
    
    graph = [[] for _ in range(N + 1)]
    
    
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if math.gcd(i, j) == 1:
                
                graph[i].append(j)
                graph[j].append(i)
                
   
    output = []
    idx = 2 
    for _ in range(Q):
        X = int(input_data[idx])
        K = int(input_data[idx+1])
        idx += 2
        
       
        if K <= len(graph[X]):
            output.append(str(graph[X][K - 1]))
        else:
            output.append("-1")
            
   
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    solve()