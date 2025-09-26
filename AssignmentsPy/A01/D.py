n = int(input())

def sorted (arr,l):
    if l==len(arr)-1:
        return True
    if arr[l]>arr[l+1]:
        return False
    return sorted(arr,l+1)


for i in range (n):
    line = input()            
    arr = [int(x) for x in line.split()]
    
    if (sorted(arr,0)):
       print("YES")
    else:
        print("NO")

    
    