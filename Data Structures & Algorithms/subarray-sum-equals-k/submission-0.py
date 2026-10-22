class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        nums=[1,2,1,2], k=3
              0 1 2 3
        """
        prefix_sum={0:1}
        current_sum=0 #0->1
        result=0
        for num in nums:
            current_sum+=num
            needed_sum=current_sum-k
            result+=prefix_sum.get(needed_sum,0)
            prefix_sum[current_sum]=prefix_sum.get(current_sum,0)+1
        return result

        