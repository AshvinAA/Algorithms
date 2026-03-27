x=1342
y=5678


def karatsubaMultiplication(x,y):
    if(len(str(x))==1 and len(str(y)) == 1):
        return x*y
    m=len 
    a=x//10
    b=x%10
    c=y//10
    d=y%10

    ac= karatsubaMultiplication(a,c)
    
    bd = karatsubaMultiplication(b,d)
    
    abcd = karatsubaMultiplication(a+b,c+d)

    adbc= abcd - ac - bd

    return 100*ac + 10*adbc + bd

print(karatsubaMultiplication(x,y))