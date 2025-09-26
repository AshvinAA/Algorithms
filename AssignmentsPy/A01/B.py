n= int(input(""))

def subtract(x,y):
    return x-y

def add(x,y):
    return x+y

def div(x,y):
    return x/y

def mul(x,y):
    return x*y

for i in range (n):
    str = input("")
    arr = str.split()
    operator= arr[2]
    x=float(arr[1])
    y=float(arr[3])

    match operator:
        case '+':
            print(add(x,y))
        case '-':
            print(subtract(x,y))
        case '*':
            print(mul(x,y))
        case '/':
            print(div(x,y))
        

