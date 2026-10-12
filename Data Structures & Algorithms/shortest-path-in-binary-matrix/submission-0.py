from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        n=len(grid)
        directions=[
            (-1,-1),(-1,0),(-1,1),
            (0,-1),        (0,1),
            (1,-1),(1,0),(1,1)
            ]
        # length of shortest clear path (0,0) -> (n-1,n-1)
        # return -1 if there is no clear path
        # thinking of using BFS because the first time we reach the bottom-right cell, we've found the shortest 
        visited_nodes=set((0,0)) #mark as visted before adding to the queue
        # we need to store the coordinate and its distance from (0,0), as this problem counts cells in the path, the beginning distance is 1
        queue=deque([(0,0,1)])
        while queue:
            r,c,distance=queue.popleft()
            # check if we reach the destination
            if r==n-1 and c==n-1:
                return distance
            # explore neighbours of current node
            for dr,dc in directions:
                x=r+dr
                y=c+dc
                #when we found an unvisited node-> check if it's still within the grid+ open (0 value) node -> its distance is cur distance +1
                if (0<=x<n and 0<=y<n and (x,y) not in visited_nodes and grid[x][y]==0):
                    # add to the queue and mark as visited
                    queue.append((x,y,distance+1))
                    visited_nodes.add((x,y))
                
        return -1
            

      
        