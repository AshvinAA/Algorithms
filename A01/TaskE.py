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



def reverseSorting():
    oddList=[]
    evenList=[]
    
    for i in range (len(arr)):
        if i%2==0:
            evenList.append(arr[i])
        else:
            oddList.append(arr[i])


def reverseSorting():
    while True:
        swap_count=0       
        swapped_index=[]
        for i in range(0 , len(arr)-2 , 1):
            swap=False
            if(arr[i] > arr[i+2]):
                swap(arr,i,i+2)
                swap_count+=1
                swapped_index.append([i+1 , i+3])
                swap=True
        if(sorted_check(arr)):
            print("YES")
            print(swap_count)
            print(swapped_index)
            return
        else:
            if(swap == False):
                print("NO")
                return
            else:
                swapped_index=[]
                swap_count=0
        
        
if(len(arr)<=2):
    if(sorted_check(arr)):
        print("YES")
        print(0)
    else:
        print("NO")
else:
    reverseSorting()