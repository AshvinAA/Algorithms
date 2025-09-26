n=int(input())
line=input()
arr = [int(x) for x in line.split()]

def parity(arr,i,j):
    if(arr[i]%2==0 and arr[j]%2==0):
        return True
    else:
        if(arr[i]%2!=0 and arr[j]%2!=0):
            return True
        else:
            return False
        
def swap(arr,l,r):
    temp=arr[l]
    arr[l] = arr[r]
    arr[r] =temp

for i in range (len(arr)-1 , 0 , -1):
    for j in range (0,i):
        if parity(arr,j,j+1) and arr[j]>arr[j+1]:
            swap(arr,j,j+1)

print(arr)