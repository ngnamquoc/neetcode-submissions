# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        # use BFS as we need to traverse every level sequentially
        output=[]
        depth_dict={}
        queue=deque([(1,root)])
        while queue:
            depth,node=queue.popleft()
            if depth not in depth_dict:
                depth_dict[depth]=[node.val]
            else:
                depth_dict[depth].append(node.val)
            if node.left is not None:
                queue.append((depth+1,node.left))
            if node.right is not None:
                queue.append((depth+1,node.right))

        # traverse the dict and add to output
        for depth, nodes in depth_dict.items():
            output.append(nodes)
        return output
     


        