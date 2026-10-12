from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # find surrounded regions first (none of the 'O' cells in that region are on the edge of the board) -> replace that region with "X"s
        #if that region has any cell on the edge -> we mark the whole region as safe -> don't eplace that region with "X"s

        # dirs with 4 dirs: up, down, left, right
        dirs=[(-1,0),(1,0),(0,-1),(0,1)]
      
        row=len(board)
        col=len(board[0])
   
        # traverse the grid
        queue=deque([])
        visited_cells=set()
        
        for i in range(row):
            for j in range(col):
                # if found a land, try to explore the neighbours
                touch_edges=False
                if (i,j) not in visited_cells and board[i][j]=="O":
                    # check if this cell touch edge
                    if i==0 or i==row-1 or j==0 or j==col-1:
                        touch_edges=True

                    region=set()
                    queue.append((i,j))
                    region.add((i,j))
                    visited_cells.add((i,j))
                    while queue:
                        r,c=queue.popleft()
                        # explore
                        for dr,dc in dirs:
                            # if found a connect cell
                            if 0<=r+dr<row and 0<=c+dc<col and (r+dr,c+dc) not in visited_cells and board[r+dr][c+dc]=="O":
                                # add to queue
                                queue.append((r+dr,c+dc))
                                visited_cells.add((r+dr,c+dc))
                                # add to region
                                region.add((r+dr,c+dc))
                                # check touch edges
                                if r+dr==0 or r+dr==row-1 or c+dc==0 or c+dc==col-1:
                                    touch_edges=True
                    # if non cell on the edge, capture it
                    if not touch_edges:
                        for x,y in region:
                            board[x][y]="X"
             

                            




  
        