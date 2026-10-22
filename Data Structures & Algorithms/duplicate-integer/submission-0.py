class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_track={}
        for num in nums:
            freq_track[num]=freq_track.get(num,0)+1
            if freq_track[num]>1:
                return True
        return False
        