class Solution:
    def jump(self, nums: List[int]) -> int:
        #        0 1 2 3 4 5
        #nums = [2,4,1,1,1,1]
        #        i^
        #farthest=0->2
        #jump_counter=0->1
        #cur_end=0
        n=len(nums)
        farthest=0
        jump_counter=0
        cur_end=0

        for jump_pos in range(n-1):
            farthest=max(farthest,jump_pos+nums[jump_pos])
            if jump_pos==cur_end:
                jump_counter+=1
                cur_end=farthest
            if cur_end >= n-1:
                break
        return jump_counter


        #time: O(n)
        #space: O(1)

        