import sys 

input,output= sys.stdin.readline , sys.stdout.write
N,E=map(int, input().split())

nodes=[0 for _ in range(N)]

u=list(map(int, input().split()))
v=list(map(int, input().split()))

for i in range(E):
    nodes[ u[i] -1 ]+=1
    nodes[ v[i] -1 ]+=1

oddCount=0

for edgeCount in nodes:
    if(edgeCount%2)==1:
        oddCount+=1

if(oddCount>2):
    output("NO")
else:
    output("YES")