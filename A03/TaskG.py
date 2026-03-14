#220 Trees

import sys
from collections import deque


input,output= sys.stdin.readline , sys.stdout.write
n = int(input())
inOrderTree = list(map(int, input().split()))
preOrderTree = list(map(int, input().split()))

def get_PostOrder(preOrder , inOrder):
    if not preOrder or not inOrder:
        return []
    
    root_val=preOrder[0]
    
    root_idx=preOrder.index(root_val)
    
    #splitting InOrder array
    
    left_inOrder = inOrder[:root_idx]
    right_inOrder = inOrder[root_idx+1:]
    
    #splitting PostOrder array
    
    left_len = len(left_inOrder)
    
    left_preOrder = preOrder[1:1+left_len]
    right_preOrder = preOrder[1+left_len:]
    
    #getting right/left PostOrder array
    left_post = get_PostOrder(left_preOrder,left_inOrder)
    right_post=get_PostOrder(right_preOrder,right_inOrder)
    
    #returning post order = L R root
    return left_post + right_post + [root_val]
    
postOrderTree=get_PostOrder(preOrderTree,inOrderTree)
print(*postOrderTree)