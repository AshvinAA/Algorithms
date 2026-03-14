#220 Trees Reassessed

import sys

sys.setrecursionlimit(2000)

input,output= sys.stdin.readline , sys.stdout.write
n = int(input())
inOrderTree = list(map(int, input().split()))
postOrderTree = list(map(int, input().split()))

def get_PreOrder(postOrder , inOrder):
    if not postOrder or not inOrder:
        return []
    
    root_val=postOrder[len(postOrder)-1]
    
    root_idx=inOrder.index(root_val)
    
    #splitting InOrder array
    
    left_inOrder = inOrder[:root_idx]
    right_inOrder = inOrder[root_idx+1:]
    
    #splitting postOrder array
    
    right_len = len(right_inOrder)
    left_len = len(left_inOrder)
    
    left_postOrder = postOrder[len(postOrder)-1-right_len-left_len:len(postOrder)-1-right_len]
    right_postOrder = postOrder[len(postOrder)-1-right_len :len(postOrder)-1]
    
    #getting right/left preOrder array
    left_post = get_PreOrder(left_postOrder,left_inOrder)
    right_post=get_PreOrder(right_postOrder,right_inOrder)
    
    #returning post order = root L R
    return [root_val] + left_post + right_post
    
preOrderTree=get_PreOrder(postOrderTree,inOrderTree)
output(" ".join(map(str, preOrderTree)) + "\n")