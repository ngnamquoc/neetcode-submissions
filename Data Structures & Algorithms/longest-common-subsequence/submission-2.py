class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """ 
                0 1 2
        text1=c a t
                c
                0 1 2 3 4    
        text2=c r a b t
                r
        dp[i][j] is longest comment subsequence between text1[:c] and text2[:r]

                                    c 
                            0      1  2  3
                            empty  c ca car
                0 empty      0     0  0  0
            r   1 c          0     1  1  1  
                2 cr         0     1  1  2
                3 cra        0     1  2  2
                4 crab       0     1  2  2
                5 crabt      0     1  2  2
        
        base cases:
        dp[0][c]=0 and dp[r][0]=0
        2 cases: 
        - last char match: if text1[c-1]==text2[r-1] -> dp[r][c]=1+dp[r-1][c-1]
        - last char unmatched: if text1[c-1]!=text2[r-1] -> max(dp[r-1][c],dp[r][c-1])
        """ 
    
        row=len(text1)+1
        col=len(text2)+1
        grid=[[0 for _ in range(col)] for _ in range(row)]
        for r in range(row):
            for c in range(col):
                if r==0 or c==0:
                    continue
                else:
                    if text1[r-1]==text2[c-1]:
                        grid[r][c]=1+grid[r-1][c-1]
                    else:
                        grid[r][c]=max(grid[r-1][c],grid[r][c-1])
        print(grid)
        return grid[row-1][col-1]

        #time: O(len(text1)*len(text2))
        #space: O(len(text1)*len(text2))
         
