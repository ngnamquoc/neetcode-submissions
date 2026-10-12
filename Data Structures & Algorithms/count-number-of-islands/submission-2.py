from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS might be suitable here
        row=len(grid)
        col=len(grid[0])
        count=0
        visited_island=set()
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1" and (i,j) not in visited_island:
                    count+=1
                    visited_island.add((i,j))
                    # run BFS to explore near by lands (use queue)
                    queue=deque([(i,j)])
                    while queue:
                        r,c=queue.popleft()
                        # explore 4 neighbors:
                        #up
                        if r-1>=0:
                            # check
                            if grid[r-1][c]=="1" and (r-1,c) not in visited_island:
                                visited_island.add((r-1,c))
                                queue.append((r-1,c))
                        #down
                        if r+1<row:
                            # check
                            if grid[r+1][c]=="1" and (r+1,c) not in visited_island:
                                visited_island.add((r+1,c))
                                queue.append((r+1,c))
                        #left
                        if c-1>=0:
                            # check
                            if grid[r][c-1]=="1" and (r,c-1) not in visited_island:
                                visited_island.add((r,c-1))
                                queue.append((r,c-1))
                        #right
                        if c+1<col:
                            # check
                            if grid[r][c+1]=="1" and (r,c+1) not in visited_island:
                                visited_island.add((r,c+1))
                                queue.append((r,c+1))
                        
        return count
        #time: O(r*c)
        #space:  O(r*c)                 

                        




        