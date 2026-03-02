import sys

#INCOMPLETE

s = sys.stdin.readline()
nums = list(map(int , sys.stdin.readline().split()))

def merge(left_arr,right_arr,arr):
    l=0
    r=0
    count=0
    

    while(l<len(left_arr) and r<len(right_arr)):
        if(left_arr[l] < right_arr[r]):
            arr.append(left_arr[l])
            l+=1
    
        else:
            arr.append(right_arr[r])
            r+=1
            if(left_arr[l] > right_arr[r]**2 ):
                count+=1
            

    while(l<len(left_arr)):
        arr.append(left_arr[l])
        l+=1
    
    while(r<len(right_arr)):
        arr.append(right_arr[r])
        r+=1

    return count


def mergeSort(arr):
    if(len(arr) <=1):
        return arr

    midPoint= len(arr)//2

    leftArr = arr[:midPoint]
    rightArr = arr[midPoint:]

    l= mergeSort(leftArr)
    r= mergeSort(rightArr)
    arr=[]

    count=0 

    inversionCount = merge(l,r,arr)
    count+=inversionCount

    return arr,count


print(mergeSort(nums))