# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, node: Optional[TreeNode],remaining:int) ->bool:
        if node is None:
            return False
        remaining-=node.val
        # if this is a leaf node, check remaining
        if node.left is None and node.right is None:
            if remaining==0:
                return True
            else:
                return False
        # if not leaf node
        return self.DFS(node.left,remaining) or self.DFS(node.right,remaining)
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # preOrder traversal: root, left, right
        # carry to the remaining sum downstream
        # if the remaining at leaf is 0 then return True
        found=self.DFS(root,targetSum)
        return found
        