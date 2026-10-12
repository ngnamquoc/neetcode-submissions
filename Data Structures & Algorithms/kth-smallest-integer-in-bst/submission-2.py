# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def DFS(self,node: Optional[TreeNode], values:list[int],k:int) -> None:
        # left,node,right
        if node is None or len(values)==k:
            return 
        self.DFS(node.left,values,k)
        if len(values)==k:
            return
        values.append(node.val)
        self.DFS(node.right,values,k)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # sort in ascending order, then kth position meaning k smallest value
        # DFS inorder traversal could print BST in ascending order, then return index k-1
        values=[]
        self.DFS(root,values,k)
        return values[k-1]
        # time: O(n)
        #space: O(n)
        