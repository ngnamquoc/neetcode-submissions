# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # helper function
    def DFS(self,node: Optional[TreeNode])->int:
        # post-order traversal
        if node is None:
            return 0
        left_height=self.DFS(node.left)
        right_height=self.DFS(node.right)
        # update diameter before returning height at current node
        self.diameter=max(self.diameter,left_height+right_height)

        return 1+max(left_height,right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # at every node, we want to get its height and max diameter
        # get the height -> use post-order traversal DFS
        #use recursion to achieve O(n) time complexity

        # global var
        self.diameter=0
        # call helper function
        self.DFS(root)
        return self.diameter

        
        
       

        

            
        