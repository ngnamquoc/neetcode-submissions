class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i] is the max amount of money we can rob from house 0 through i without robbing adjacent houses
        #we have two choices at house i, rob house i and skip house i
        #case we decide to rob house i
        # rob_current= dp[i-2]+nums[i-1]
        #case we decide not to rob house i
        # skip_current=dp[i-1]
        #finally choose the best answer
        # dp[i]=max(rob_current,skip_current)
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            rob_current=dp[i-2]+nums[i]
            skip_current=dp[i-1]
            dp[i]=max(rob_current,skip_current)
        return dp[-1]


        