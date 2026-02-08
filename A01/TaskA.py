import sys

number_of_inputs=int(sys.stdin.readline())
numbers=[]
for i in range (number_of_inputs):
    numbers.append(int(sys.stdin.readline()))


for num in numbers:
    if num%2 == 0:
        print(f'{num} is an Even number.')
    else:
        print(f'{num} is an Odd number.')

