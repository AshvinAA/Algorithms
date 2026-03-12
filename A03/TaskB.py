#COUNT THE INVERSION REVISITED
import bisect

import sys


input,output= sys.stdin.readline , sys.stdout.write

n = int(input())
arr = list(map(int, input().split()))

matches=[]
count=0

for i in range(n-1 , -1 , -1):
    index = bisect.bisect_left(matches, arr[i])
    count+=index
    bisect.insort(matches , arr[i]**2)


output(str(count))