# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def DFS(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        # post-order traversal to get the left and right sub-tree height
        left_height=self.DFS(node.left)
        right_height=self.DFS(node.right)
        if abs(left_height-right_height)>1:
            self.isBalance=False
        return 1+max(left_height,right_height)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalance=True
        tree_height=self.DFS(root)
        print("height of the tree is: ",tree_height)
        return self.isBalance
        