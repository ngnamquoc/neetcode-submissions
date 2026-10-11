# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def DFS(self,node: Optional[TreeNode]) -> list[int]:
        # left,node,right
        if node is None:
            return []
        left_values=self.DFS(node.left)
        right_values=self.DFS(node.right)
        return left_values + [node.val] + right_values
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # sort in ascending order, then kth position meaning k smallest value
        # DFS inorder traversal could print BST in ascending order, then return index k-1
        sorted_list=self.DFS(root)
        return sorted_list[k-1]
        # time: O(n)
        #space: O(n)
        