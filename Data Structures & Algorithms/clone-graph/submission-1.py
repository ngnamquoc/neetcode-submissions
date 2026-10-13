"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # return a clone starting node, gragh doesn't necessarily have root -> so we call this as starting node
        # use a dic to keep track corresponding cloned node to original list
        if node is None:
            return node
        clone_track=dict()
        clone_track[node]=Node(node.val)
        # we don't assign original neighbors to starting_clone_node since it contains references to the original nodes
        # use BFS
        queue=deque([node])
        while queue:
            current=queue.popleft()
            for neighbor in current.neighbors:
                # create a clone if not existed
                if neighbor not in clone_track:
                    clone_track[neighbor]=Node(neighbor.val)
                    queue.append(neighbor)
                # don't need to create clone if already existed
                clone_track[current].neighbors.append(clone_track[neighbor])
        return clone_track[node]
                

       
        