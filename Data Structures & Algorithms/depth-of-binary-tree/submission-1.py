# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        # we will use DFS as the goal is to reach the heighest node
        #DFS will use stack, add right, then left to pop left first
        if root is None:
            return 0
        stack=[(root,1)]
        max_depth=1
        while stack:
            node,depth=stack.pop()
            if node.right is not None:
                stack.append((node.right,depth+1))
                max_depth=max(max_depth,depth+1)
            if node.left is not None:
                stack.append((node.left,depth+1))
                max_depth=max(max_depth,depth+1)
        return max_depth

      
        