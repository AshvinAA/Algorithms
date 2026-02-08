import sys

inputs = int(sys.stdin.readline())
arr=[]
for i in range(inputs):
    arr.append(int(sys.stdin.readline()))
    
for num in arr:    
    print( int((num**2 + num)/2) )