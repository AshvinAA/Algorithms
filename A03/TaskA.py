import sys
#Count the Inversion

s = sys.stdin.readline()
nums = list(map(int , sys.stdin.readline().split()))

def merge(left_arr,right_arr):
    l=0
    r=0
    inversionCount=0
    arr=[]

    while(l<len(left_arr) and r<len(right_arr)):
        if(left_arr[l] < right_arr[r]):
            arr.append(left_arr[l])
            l+=1
        else:
            arr.append(right_arr[r])
            r+=1
            inversionCount += (len(left_arr) - l)

    while(l<len(left_arr)):
        arr.append(left_arr[l])
        l+=1
    
    while(r<len(right_arr)):
        arr.append(right_arr[r])
        r+=1

    return arr,inversionCount
        
def mergeSort(arr):
    if(len(arr) <=1):
        return arr,0
    mid= len(arr)//2

    leftArr = arr[:mid]   
    rightArr = arr[mid:]

    
    l,n=mergeSort(leftArr)
    r,k=mergeSort(rightArr)
    merged_arr, iCount = merge(l, r)
    total_inversions = n + k + iCount

    return merged_arr, total_inversions

arr,count=mergeSort(nums)
print(count)
print(*arr)
    