import sys
number_of_inputs  = int(sys.stdin.readline())


def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y


def operation(num1, num2 , operator):
    if operator == '+':
        return add(num1,num2)
    elif operator == '-':
        return sub(num1,num2)
    elif operator == '/':
        return div(num1, num2)
    elif operator == '*': 
        return mul(num1,num2)

commands=[]

for i in range(number_of_inputs):

    arr = sys.stdin.readline().split()
    commands.append(arr)
    
    
    
for arr in commands:
    num1= float(arr[1])
    num2= float(arr[3])
    operator = arr[2]
    print(operation(num1 , num2 , operator) )

