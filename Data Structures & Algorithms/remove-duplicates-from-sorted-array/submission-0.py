class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1

        unique=0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                unique+=1
                nums[unique]=nums[i]
        
        return len(nums[:unique+1])

        