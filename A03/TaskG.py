#220 Trees

import sys
from collections import deque
class Node:
    def __init__(self,rt):
        rt=self.rt
        l=self.l
        r=self.r

input,output= sys.stdin.readline , sys.stdout.write
n = int(input())
inOrderTree = list(map(int, input().split()))
preOrderTree = list(map(int, input().split()))

def treeBuilder(preStart,preEnd,inStart,inEnd,inOrderTree,preOrderTree,element):
    if(inStart == inEnd):
        return Node(preOrderTree[inStart])
    
    node=Node(preOrderTree[preStart])
    
    iSL=0
    iEL=inOrderTree.index(element)-1
    pSL=preOrderTree.index(element)+1
    pEL=pSL+iEL+1
    node.left=treeBuilder(pSL,pEL,iSL,iEL,inOrderTree,preOrderTree)