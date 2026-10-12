# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, node: Optional[TreeNode],remaining:int) ->bool:
        if node is None: # for case where a node has 1 child and 1 null child
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
    # time: O(n) where n is No. of nodes
    #space:O(h) where h is the tree height as we need to maintain the recursive call stack-> balanced tree case O(logn) and skewed tree is O(n)
        