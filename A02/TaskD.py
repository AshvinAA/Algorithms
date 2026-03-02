#Beautiful Sorted List

M=int(input())
l=list(map(int,input().split()))
N=int(input())
x=list(map(int,input().split()))
a=[]
i=0
j=0
while i<M and j<N:
    if l[i]<x[j]:
        a.append(l[i])
        i+=1
    else:
        a.append(x[j])
        j+=1
while i<M:
    a.append(l[i])
    i+=1
while j<N:
    a.append(x[j])
    j+=1
print(*a)
        