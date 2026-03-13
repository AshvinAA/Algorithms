#FAST POWER DRIFT

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
        
        
a,b = map(int, input().split())

output(str(fast_power_drift(a,b,107)))

