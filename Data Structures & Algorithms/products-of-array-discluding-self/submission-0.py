class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[1]*n
        right=[1]*n
        product_except=[]
        left_product=1
        right_product=1
        for i in range(1,n):
            left_product*=nums[i-1]
            left[i]=left_product

        for i in range(n-2,-1,-1):
            right_product*=nums[i+1]
            right[i]=right_product
        
        for i in range(n):
            product_except.append(left[i]*right[i])

        return product_except 
        