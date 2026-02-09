import sys


def swap(arr , x , y):
    temp = arr[x]
    arr[x]=arr[y]
    arr[y]=temp
    
inputs=int(sys.stdin.readline()) #1

for k in range(inputs):


    no_of_students=int(sys.stdin.readline())
    
    id_num= list(map(int ,sys.stdin.readline().split()))
    marks= list(map(int ,sys.stdin.readline().split()))

    swap_count=0
    
    N= len(id_num)
    for i in range(N):
            best_idx = i
            
            for j in range(i + 1, N):
                
                if marks[j] > marks[best_idx]:
                    best_idx = j
                
                elif marks[j] == marks[best_idx]:
                    if id_num[j] < id_num[best_idx]:
                        best_idx = j
            
            
            if best_idx != i:
                swap(marks, i, best_idx)
                swap(id_num, i, best_idx)
                swap_count += 1

    output=[]
    output.append(f"Minimum swaps: {swap_count}")
    for k in range(N):
        output.append(f"ID: {id_num[k]} Mark: {marks[k]}")
    sys.stdout.write("\n".join(output) + "\n")

