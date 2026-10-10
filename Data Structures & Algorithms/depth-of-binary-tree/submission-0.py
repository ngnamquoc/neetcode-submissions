# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def DFS(self,node: TreeNode):
        if node is None:
            return 0
        return 1 + max(self.DFS(node.left),self.DFS(node.right))
    def maxDepth(self, root: TreeNode | None) -> int:
        # use post order traversal
        return self.DFS(root)
        