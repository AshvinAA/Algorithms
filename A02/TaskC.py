#Triple the Trouble 

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))

arr = [(a[i], i + 1) for i in range(n)]

arr.sort()


for i in range(n):
    target = x - arr[i][0]
    l, r = i + 1, n - 1
    while l < r:
        total = arr[l][0] + arr[r][0]
        if total == target:
            print(arr[i][1], arr[l][1], arr[r][1])
            sys.exit()
        elif total < target:
            l += 1
        else:
            r -= 1

print(-1)