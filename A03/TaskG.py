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


element=preOrderTree[0]
root = Node(element)

left= inOrderTree[0:preOrderTree.index(element)]
right= inOrderTree[preOrderTree.index(element):n-1]

def treeBuilder(preStart,preEnd,inStart,inEnd,inOrderTree,preOrderTree,root):
    pass 