import sys 

input,output= sys.stdin.readline , sys.stdout.write
N=input().split()

#putting all 0s in the array
matrix = [[0 for _ in range(N)] for _ in range(N)]