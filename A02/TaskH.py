import sys

input = int(sys.stdin.readline())

for i in range (input):

    arr= list(map(int , sys.stdin.readline().split()))

    target = arr[0]
    number = arr[1]

    l=0
    r=target * number
    m=(l+r)//2


    while(True):
        m=(l+r)//2
        num = m - int(m//number)
        if( num == target):
            print(m)
            break
        elif( num < target ):
            l=m+1
            
        elif(num > target):
            r=m-1
            
