class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_len=0
        last_seen={}
        left=0

        for right in range(len(s)):
            # case duplication
            if s[right] in last_seen and last_seen[s[right]] >= left:
                # fix left
                left=last_seen[s[right]]+1
            # both cases
            last_seen[s[right]]=right
            cur_substring_len=right-left+1
            longest_substring_len=max(longest_substring_len,cur_substring_len)
        
        return longest_substring_len
            
        