#Two Sum Trouble

n=list(map(int,input().split()))
l=list(map(int,input().split()))
i=0
j=len(l)-1
res=None
while(i<j):
    sumNum=l[i]+l[j]   #adding l and r
    if(sumNum==n[1]):
        res=[i+1,j+1]
        break
    elif sumNum<n[1]:
        i+=1
    else:
        j-=1
if res:
    print(*res)
else:
    print(-1)