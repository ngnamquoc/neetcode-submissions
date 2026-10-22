class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence_len=0
        num_set=set(nums)
        for num in nums:
            if num-1 not in num_set:
                cur_sequence_len=1
                while True:
                    if num+1 in num_set:
                        cur_sequence_len+=1
                        num+=1
                        longest_sequence_len=max(longest_sequence_len,cur_sequence_len)
                    else:
                        longest_sequence_len=max(longest_sequence_len,cur_sequence_len)
                        break
        return longest_sequence_len
            
        