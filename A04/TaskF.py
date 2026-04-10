#KING MOVES

import sys 

input,output= sys.stdin.readline , sys.stdout.write
n=int(input())
x,y=map(int, input().split())

def validMove(x,y,n):
    if(x<0 or x>=n or y<0 or y>=n):
        return False
    return True


def moves(x,y,n):
    turns=[]

    if(validMove(x-1,y-1,n)):turns.append((x-1+1,y-1+1))
    if(validMove(x-1,y,n)):turns.append((x-1+1,y+1))
    if(validMove(x-1,y+1,n)):turns.append((x-1+1,y+1+1))
    if(validMove(x,y-1,n)):turns.append((x+1,y-1+1))
    if(validMove(x,y+1,n)):turns.append((x+1,y+1+1))
    if(validMove(x+1,y-1,n)):turns.append((x+1+1,y-1+1))
    if(validMove(x+1,y,n)):turns.append((x+1+1,y+1))
    if(validMove(x+1,y+1,n)):turns.append((x+1+1,y+1+1))
        

    return turns

turns  = moves(x-1,y-1,n)

output(str(len(turns))+"\n")

for row in turns:
    output(" ".join(map(str,row))+"\n")
    
    

    