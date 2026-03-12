import sys
from collections import deque

input,output= sys.stdin.readline , sys.stdout.write
n = int(input())
arr = list(map(int, input().split()))
new_arr=[]
stack= deque()
stack.append((0,n-1))

while len(stack)!=0:
    l, r = stack.pop()
    
    if(l>r):
        continue
    
    mid=(l+r)//2
    
    new_arr.append(arr[mid])
    
    left=(l,mid-1)
    right=(mid+1,r)
    
    stack.append(left)
    stack.append(right)

output(" ".join(map(str, new_arr)) + "\n")