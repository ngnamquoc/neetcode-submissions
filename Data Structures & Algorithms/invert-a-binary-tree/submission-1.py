# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        # try with BFS
        queue=deque([root])
        while queue:
            node=queue.popleft()
            # swap left and right node 
            node_left=node.left
            node.left=node.right
            node.right=node_left
            # add to queue
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return root

        # space: O(w) for w is the max width three level
        #time: O(n)
        

        
            
        