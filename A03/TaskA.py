import sys
#INCOMPLETE

s = sys.stdin.readline()
nums = list(map(int , sys.stdin.readline().split()))

def merge(left_arr,right_arr,arr[]):
    l=0
    r=0
    inversionCount=0

    while(l<len(left_arr) and r<len(right_arr)):
        if(left_arr[l] < right_arr[r]):
            arr.append(left_arr[l])
            l+=1
        else:
            arr.append(right_arr[r])
            r+=1
            inversionCount+=1

    while(l<len(left_arr)):
        arr.append(left_arr[l])
        l+=1
    
    while(r<len(right_arr)):
        arr.append(right_arr[r])
        r+=1

    return inversionCount
        
def mergeSort(arr):
    if(len(arr) <=1):
        return arr
    
    leftArr=[]
    rightArr=[]

    x=0

    for num in arr:
        if(x< len(arr)/2):
            leftArr.append(num)
            x+=1
        else:
            rightArr.append(num)
    inversionCounts=0
    arr=[]
    l=mergeSort(leftArr)
    r=mergeSort(rightArr)
    inversionCounts+=merge(l,r,arr)
    return inversionCounts

print(mergeSort(nums))
    