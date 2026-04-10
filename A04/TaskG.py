#KNIGHT CLASH

import sys 

input,output= sys.stdin.readline , sys.stdout.write

r,c,numKnights=map(int, input().split())

def validMove(x,y,r,c):
    if(x<0 or x>=r or y<0 or y>=c):
        return False
    return True

#storing the current knight positions
positions = set()

for _ in range(numKnights):
    x, y = map(int, input().split())
    positions.add((x, y))

def conflict(positions):
    for x,y in positions:
        available_moves=[(x-2,y+1),
                        (x-1,y+2),
                        (x+2,y+1),
                        (x+1,y+2),
                        (x-2,y-1),
                        (x-1,y-2),
                        (x+1,y-2),
                        (x+2,y-1)
                        ]
        #checking for all the valid moves for one position
        for move in available_moves:
            if(validMove(x,y,r,c)):
                if move in positions:
                    return True
    return False




if(conflict(positions)==True):output("YES")
else:output("NO")

    

    






        




    
    

    