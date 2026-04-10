#ADJACENCY MATRIX REPRESENTATION

import sys 

input,output= sys.stdin.readline , sys.stdout.write
N,E=map(int, input().split())

#putting all 0s in the array
matrix = [[0 for _ in range(N)] for _ in range(N)]

for i in range(E):
    u,v,x=map(int, input().split())

    matrix[u-1][v-1]=x

for row in matrix:
    output(" ".join(map(str,row))+"\n")