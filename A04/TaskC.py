#ADJACENCY LIST TO MATRIX

import sys 

input,output= sys.stdin.readline , sys.stdout.write
N=int(input())

#putting all 0s in the array
matrix = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    u=list(map(int, input().split()))
    
    if(u[0] == 0 ):
        continue

    for j in range(1,len(u)):
        matrix[i][u[j]] = 1
    
for row in matrix:
    output(" ".join(map(str,row))+"\n")

        