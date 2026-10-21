class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       #col 
        #0 1 2 3 4 5
#row#0  1  1 1 1 1 1
    #1  1
    #2  1
        # row=m
        # col=n
        #initialize 2d grid
        # grid=[[1 for _ in range(col)]for _ in range(row)]
        # for r in range(1,row):
        #     for c in range(1,col):
        #         grid[r][c]=grid[r-1][c]+grid[r][c-1]
        # return grid[row-1][col-1]
        #time complexity: O(mn)
        #space: O(mn)

        #optimization
        previous=n*[1]
        current=n*[1]
        for i in range(1,m):
            for j in range(1,n):
                current[j]=previous[j]+current[j-1]
            previous=current
        return previous[-1]
        #time: O(mn)
        #space: O(n)
            




        