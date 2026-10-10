# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # we will use BFS to compare layer by layer
        # BFS use queue , first in first out -> deque.popleft
        if p is None or q is None:
            if p is None and q is None:
                return True
            else:
                return False
        queue1=deque([p])
        queue2=deque([q])
        while queue1 and queue2:
            node1=queue1.popleft()
            node2=queue2.popleft()
            if node1.val!=node2.val:
                return False
            # check if any tree is missing left,right node
            if (node1.left is None) != (node2.left is None):
                return False
            if (node1.right is None) != (node2.right is None):
                return False
            # add left
            if node1.left is not None:
                queue1.append(node1.left)
            if node2.left is not None:
                queue2.append(node2.left)
            # add right
            if node1.right is not None:
                queue1.append(node1.right)
            if node2.right is not None:
                queue2.append(node2.right)


        # if length of 2 the same, then True
        if len(queue1)==len(queue2):
            return True
        else:
            return False
        
            
        