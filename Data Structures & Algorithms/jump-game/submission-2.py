class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #        0 1 2 3 4
        #nums = [1,2,0,1,0]
        #               i
        #n=5
        farthest=0
        for cur_jump_position in range(len(nums)):
            if cur_jump_position>farthest:
                return False
            farthest=max(farthest,cur_jump_position+nums[cur_jump_position])
        return True


        