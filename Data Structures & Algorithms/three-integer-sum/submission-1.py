class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        nums.sort()
        n=len(nums)
        for i in range(0,n):
            #skip index if it has similar value as the previous one to avoid duplicate value in the output
            if i>0 and nums[i]==nums[i-1]: 
                continue
            left=i+1
            right=n-1
            while left<right:
                cur_sum=nums[left]+nums[right]
                if cur_sum < -nums[i]:
                    left+=1
                elif cur_sum > -nums[i]:
                    right-=1
                else:
                    result=[nums[i],nums[left],nums[right]]
                    output.append(result)
                    # move both inward since we used both numbers
                    left+=1
                    right-=1
                     # skip duplicate left
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    # skil duplicate right
                    while left<right and nums[right]==nums[right+1]:
                        right-=1

        return output
   
  


        