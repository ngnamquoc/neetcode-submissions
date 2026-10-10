# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # edge case
        if root is None:
            return []
        queue=deque([root])
        output=[]
        while queue:
            level=[]
            level_size=len(queue)
            # keep adding to level until level_size=0
            # for every node got pop to level, add its left right nodes
            while level_size>0:
                cur_node=queue.popleft()
                level.append(cur_node.val)
                level_size-=1

                if cur_node.left is not None:
                    queue.append(cur_node.left)
                if cur_node.right is not None:
                    queue.append(cur_node.right)
                
            output.append(level)
            

        return output


        