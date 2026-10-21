class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        """
        r=len(obstacleGrid)
        c=len(obstacleGrid[0])
            0  1 
        0   [1,0],

             0  1 
        0   [1,1],

        """
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
        grid=[[1 for _ in range(col)] for _ in range(row)]

        for r in range(row):
            for c in range(col):
                #case border row or col
                if r==0 or c==0:
                    if obstacleGrid[r][c]==1:
                        grid[r][c]=0
                    else:
                        if r==0 and c>0:
                            #copy from the left 
                            grid[r][c]=grid[r][c-1]
                        elif c==0 and r>0:
                            #copy from above
                            grid[r][c]=grid[r-1][c]

                else:
                    if obstacleGrid[r][c]==1:
                        grid[r][c]=0
                    else:
                        grid[r][c]=grid[r-1][c]+grid[r][c-1]
        return grid[row-1][col-1]

        