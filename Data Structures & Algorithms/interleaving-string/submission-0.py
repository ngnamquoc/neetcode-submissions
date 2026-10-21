class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        dp[i][j]=whether s1[:j] and s2[:i] can interleave to form s3[:i+j]

        s2     s1   c 0  1  2  3   4          
        r          empty a aa aaa aaaa
        0   empty   T    T  T  F   F
        1   b       F    F  T  F   F
        2   bb      F    F  T  F   F
        3   bbb     F    F  T  F   F
        4   bbbb    F    F  T  T   F

           0123    
        s1=aaaa

           0123
        s2=bbbb 

           01234567
        s3=aabbbbaa   
        """
        row=len(s2)+1
        col=len(s1)+1
        if row+col!=len(s3)+2:
            return False
        grid=[[False for _ in range(col)] for _ in range(row)]
        for r in range(row):
            for c in range(col):
                #fill in the border row, col
                if r==0 and c==0:
                    grid[r][c]=True
                elif r==0:
                    if grid[r][c-1] and s1[c-1]==s3[r+c-1]:
                        grid[r][c]=True

                elif c==0:
                    if grid[r-1][c] and s2[r-1]==s3[r+c-1]:
                        grid[r][c]=True

                else:
                    #case 1: last char of str1 matches last char of str3
                    if grid[r][c-1] and s1[c-1]==s3[r+c-1]:
                        grid[r][c]=True
                    #case2: last char of str2 matches last char of str3
                    elif grid[r-1][c] and s2[r-1]==s3[r+c-1]:
                        grid[r][c]=True
        return grid[row-1][col-1]

            
                
        