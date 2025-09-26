n=int(input())
line1=input()
id=[int(x) for x in line1.split()]
line2=input()
marks=[int(x) for x in line2.split()]

def swapper(id,marks,l,r,count):
    if(i!=j):
        if(marks[l] == marks[r]):
            if(id[l] > id[r]):
                swap(id,l,r)
                return True
            
        else:
            if(marks[l] < marks[r] ):
                swap(marks,l,r)
                swap(id,l,r)
                return True
        return False
    return False

def swap(arr,l,r):
    temp=arr[l]
    arr[l] = arr[r]
    arr[r] =temp

swapCount=0

for i in range (len(marks)):
    for j in range (i,len(marks),+1):
        if (swapper(id,marks,i,j,swapCount)):
            swapCount+=1


print(f"Minimum swaps: {swapCount}")
for i in range (len(marks)):
    print(f"ID: {id[i]} Mark: {marks[i]}")