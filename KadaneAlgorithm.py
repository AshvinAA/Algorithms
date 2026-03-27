arr=[3,-4,5,4,-1,7,-8,9,-10,-10,20]

l=0

index=[0,0]

maximum_sum=arr[l]
current_sum=arr[l]

for r in range(1, len(arr)):

    if(arr[r] > current_sum ):
        l=r
        current_sum=arr[r]

    elif(current_sum + arr[r] > current_sum):
        current_sum+=arr[r]


    if(current_sum > maximum_sum ):
        maximum_sum = current_sum 
        index[0] = l
        index[1] = r
    
        


print("Maximum subarray is ",   arr[index[0] : index[1]+1 ])

print("Maximum sum is" , maximum_sum)