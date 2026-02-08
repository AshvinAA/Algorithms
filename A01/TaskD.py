import sys

number_of_inputs= int(sys.stdin.readline())

def sorted_check(arr):
    for i in range(0 , len(arr) - 1 , 1 ):
        if int(arr[i])>int(arr[i+1]):
            print("NO")
            return
    print("YES")
    
arrays=[]    

for i in range(number_of_inputs):
    num=int(sys.stdin.readline())
    numbers=sys.stdin.readline().split()
    arrays.append(numbers)

for arr in arrays:
    sorted_check(arr)

