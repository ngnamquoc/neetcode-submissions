# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # use BFS as we need to traverse every level
        # for every level return the rightmost existing node at that level
        if root is None:
            return []
        queue=deque([root])
        rightmost_output=[] 

        while queue:
            level_size=len(queue)
            cur_level_nodes=[]

            for _ in range(level_size):
                node=queue.popleft()
                cur_level_nodes.append(node.val)

                # add left and right to queue
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            rightmost_output.append(cur_level_nodes[-1])
        
        return rightmost_output

    # time: O(n)
    #space: O(w) for w is the max width of layers
                

        