import sys

#Parity Check: Separate the elements into two lists: one for even indices and one for odd indices.Sort them separately: Use any sorting method (since $N$ is small, your while True swap logic works).Merge them back: Put them back in their original spots.Final Check: If the resulting array is sorted, the answer is YES. If not, it's NO.

def swap(arr , x , y):
    temp = arr[x]
    arr[x]=arr[y]
    arr[y]=temp

def sorted_check(arr):
    for i in range(0 , len(arr) - 1 , 1 ):
        if int(arr[i])>int(arr[i+1]):
            return False
    return True

num= sys.stdin.readline()
arr = list(map(int, sys.stdin.readline().split()))

def sort(array):
    swapped=[]
    swap_count=0
    for i in range (len(array)):
        minIndex=i
        for j in range(i+1 , len(array)):
            if(array[j] < array[minIndex]):
                minIndex=j
                
        if(minIndex!=i):
            swapped.append([i+1 , minIndex + 1])
            swap_count+=1
            swap(array, minIndex , i )            
    return swapped,swap_count


def reverseSorting():
    oddList=[]
    evenList=[]
    
    for i in range (len(arr)):
        if i%2==0:
            evenList.append(arr[i])
        else:
            oddList.append(arr[i])
    
    evenSortedArray,evenSortedCount= sort(evenList)
    oddSortedArray,oddSortedCount= sort(oddList)
    
    newList=[]
    evenIndex=0
    oddIndex=0
    
    for i in range (len(arr)):
        if (i%2==0):
            newList.append(evenList[evenIndex])
            evenIndex+=1
        else:
            newList.append(oddList[oddIndex])
            oddIndex+=1
            
    if(sorted_check(newList)):
        print("YES")
        print(evenSortedCount + oddSortedCount)
        print(evenSortedArray)
        print(oddSortedArray)
    else:
        print("NO")

        
if(len(arr)<=2):
    if(sorted_check(arr)):
        print("YES")
        print(0)
    else:
        print("NO")
else:
    reverseSorting()