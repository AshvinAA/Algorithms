#Longest K Distinct Subarray 

# Input reading
n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = {}

left = 0
max_length = 0

for right in range(n):
    num = arr[right]
    # Add the number to our count
    count[num] = count.get(num, 0) + 1

    # If there are more than k distinct numbers, shrink the window from the left
    while len(count) > k:
        left_num = arr[left]
        count[left_num] -= 1
        if count[left_num] == 0:
            del count[left_num]  # remove from dictionary if count becomes 0
        left += 1  # move left pointer right

    # Update maximum length found so far
    max_length = max(max_length, right - left + 1)

# Output the result
print(max_length)