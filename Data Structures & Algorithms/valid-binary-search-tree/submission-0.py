# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def DFS(self, node: Optional[TreeNode], lower:int, upper:int) -> bool:
        # DFS pre-order traversal: node, left,right
        if node is None:
            return True
        if not (lower<node.val<upper):
            return False
        #check both children with updated bounds
        isValid=self.DFS(node.left,lower,node.val) and self.DFS(node.right,node.val,upper)
        return isValid
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # thinking of using DFS preOrder traversal
        isValid=self.DFS(root,float('-inf'),float('inf'))
        return isValid
        