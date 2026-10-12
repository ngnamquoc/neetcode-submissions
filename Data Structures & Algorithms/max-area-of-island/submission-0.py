from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # if not grid or not grid[0]:
        #     return 0

        row=len(grid)
        col=len(grid[0])
        visited_islands=set()
        max_area=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and (i,j) not in visited_islands:
                    area=1
                    visited_islands.add((i,j))
                    # explore near by lands if any
                    queue=deque([(i,j)])
                    while queue:
                        r,c=queue.popleft()
                        #up
                        if r-1>=0:
                            if grid[r-1][c]==1 and (r-1,c) not in visited_islands:
                                area+=1
                                visited_islands.add((r-1,c))
                                queue.append((r-1,c))
                        #down
                        if r+1<row:
                            if grid[r+1][c]==1 and (r+1,c) not in visited_islands:
                                area+=1
                                visited_islands.add((r+1,c))
                                queue.append((r+1,c))
                        #left
                        if c-1>=0:
                            if grid[r][c-1]==1 and (r,c-1) not in visited_islands:
                                area+=1
                                visited_islands.add((r,c-1))
                                queue.append((r,c-1))
                        #right
                        if c+1<col:
                            if grid[r][c+1]==1 and (r,c+1) not in visited_islands:
                                area+=1
                                visited_islands.add((r,c+1))
                                queue.append((r,c+1))
                    max_area=max(max_area,area)
        return max_area


        