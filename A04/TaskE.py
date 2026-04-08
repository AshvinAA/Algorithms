import sys 

input,output= sys.stdin.readline , sys.stdout.write
N,E=map(int, input().split())

nodes=[0 for _ in range(N)]

u=list(map(int, input().split()))
v=list(map(int, input().split()))

for i in range(E):
    nodes[u[i]-1]-=1
    nodes[v[i]-1]+=1

output(" ".join(map(str,nodes)))
