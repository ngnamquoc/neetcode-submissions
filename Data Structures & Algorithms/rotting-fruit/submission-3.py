from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # min num of minutes -> best case
        # using BFS, with 4 moving directions (up,down,left,right)
        # found 1, then mark it as 2
        #4 moving directions (up,down,left,right)
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        # because there could be multiple rotting fruits at the beginning -> scan and append all of them to queue -> multi-source BFS
        row=len(grid)
        col=len(grid[0])
        queue=deque([])
        visited=set()
        fresh_fruit_count=0
        rotting_fruit_count=0
        last_minutes=0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    queue.append((i,j,0))
                    # mark as visited
                    visited.add((i,j))
                    rotting_fruit_count+=1
                if grid[i][j]==1:
                    fresh_fruit_count+=1
        # case there is no rotting fuit
        if rotting_fruit_count==0 and fresh_fruit_count==0:
            return last_minutes
        while queue:
            r,c,minutes=queue.popleft()
            last_minutes=minutes
            # explore its neighbours
            for dr,dc in directions:
                if 0<=r+dr<row and 0<=c+dc<col and (r+dr,c+dc) not in visited and grid[r+dr][c+dc]==1:
                    # mark as rotten
                    grid[r+dr][c+dc]=2
                    # update counter
                    fresh_fruit_count-=1
                    # add to the queue and mark as visited
                    queue.append((r+dr,c+dc,minutes+1))
                    visited.add((r+dr,c+dc))
        if fresh_fruit_count==0:
            return last_minutes
        else: 
            return -1

        # time: O(V) where V is the number of cells
        #space: O(V)



        
