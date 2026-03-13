def modder(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    if(b%2==1):
        return a*modder(a,b//2)*modder(a,b//2)
    else:
        return modder(a,b//2)*modder(a,b//2)
        
        
x=modder(2,3)

print(x)