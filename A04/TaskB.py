#GRAPH METAMORPHOSIS

import sys 

input,output= sys.stdin.readline , sys.stdout.write
N,E=map(int, input().split())

u=list(map(int, input().split()))
v=list(map(int, input().split()))
values=list(map(int, input().split()))

matrix=[[] for _ in range(N)]


for i in range(E):
    node  = u[i]
    edge = v[i]
    value = values[i]

    matrix[node-1].append ((edge , value))

for i in range(N):
    row = matrix[i]
    output(str(i+1)+": ")
    output(" ".join(map(str,row))+"\n")

