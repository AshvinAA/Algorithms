n = int(input())

def sorted(arr):
    for i in range(len(arr)-1):
        if(arr[i] > arr[i+1]):
            return False
    return True

def swap(arr,l,r):
    temp=arr[l]
    arr[l] = arr[r]
    arr[r] =temp

line = input()            
arr = [int(x) for x in line.split()]
yes=False 
if(len(arr) < 3):
    if(len(arr) == 2):
        if(arr[0] <= arr[1]):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
else:
    for i in range (0,n-2):
        swap(arr,i,i+2)
        if sorted(arr):   
            print("YES")
            yes=True
            break

    if not yes:
        print("NO")



