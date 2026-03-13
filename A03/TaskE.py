#FAST SERIES DRIFT
import sys

input,output= sys.stdin.readline , sys.stdout.write

def fast_power_drift(a,b,m):
    if b==0:
        return 1
    if b==1:
        return a%m
    
    half = fast_power_drift(a,b//2,m)
    squared = (half * half)%m
    
    
    if(b%2==1):
        return (a*squared)%m
    else:
        return squared
    
n=int(input())
out="1"
for i in range(n):
    a,b,m=map(int,input().split())
    
    sum = 0 
    for i in range(1,n):
        sum+=fast_power_drift(a,i,m)
    out+=(str(sum%m)+"\n")

output(out)
    