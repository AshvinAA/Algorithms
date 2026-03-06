#Count the Numbers


import sys


number=list(map(int,sys.stdin.readline().split()))
inputs=number[1]
array = list(map(int,sys.stdin.readline().split()))


#finding the minimum index 
def leftIndex(arr , target):
    l=0
    r=len(arr)-1
    answer = len(arr)
    
    while(l<=r):
        m=(l+r)//2

        if(arr[m] >=target):
            answer = m
            r = m-1
        else:
            l = m + 1
        
    return answer
    
#finding the maximum index
def rightIndex(arr , target):
    l=0
    r=len(arr)-1
    answer = -1
    
    while(l<=r):
        m=(l+r)//2

        if(arr[m] <=target):
            answer = m
            l = m+1
        else:
            r = m - 1
        
    return answer

for i in range(inputs):
    targets = list(map(int,sys.stdin.readline().split()))
    r=rightIndex(array,targets[1])
    l=leftIndex(array,targets[0])
    
    print(r-l+1)


    
        
        