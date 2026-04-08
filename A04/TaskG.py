import sys 

input,output= sys.stdin.readline , sys.stdout.write

r,c,numKnights=map(int, input().split())

def validMove(x,y,r,c):
    if(x<0 or x>=r or y<0 or y>=c):
        return False
    return True

turns=[]

def conflict(x,y,r,c,turns):
    available_moves=[(x-2,y+1),
                     (x-1,y+2),
                     (x+2,y+1),
                     (x+1,y+2),
                     (x-2,y-1),
                     (x-1,y-2),
                     (x+1,y-2),
                     (x+2,y-1)
                     ]

    for move in available_moves:
        if(validMove(move[0] , move[1] , r , c)):

            if move in turns:
                return True
    return False

def conflict_checker(): 
    turns=[]
    for _ in range(numKnights):
        x,y=map(int, input().split())

        if(conflict(x,y,r,c,turns)==True):return True

    return False

result = conflict_checker()

if(result == True):
    output("NO")

        




    
    

    