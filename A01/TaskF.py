import sys

n = sys.stdin.readline()
arr= list(map(int , sys.stdin.readline().split()))


def swap(arr , x , y):
    temp = arr[x]
    arr[x]=arr[y]
    arr[y]=temp
    

def parity_check(x,y):
    if ((x%2==0 and y%2==0) or (x%2!=0 and y%2!=0)):
        return True
    else:
        return False


for i in range (len(arr)):

    for j in range (i+1,len(arr),1):
        
        if(arr[j] < arr[j-1]):                
            if(parity_check(arr[j] , arr[j-1])):
                swap(arr , j , j-1 )
            
print(arr)       

for num in arr:
    print(num, end=" ")