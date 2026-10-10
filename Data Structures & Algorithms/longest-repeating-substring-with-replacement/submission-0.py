class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # replacement_needed=window length - frequency of most common char
        # so if replacement_needed = k -> this window is valid
        # or window length - frequency of most common char <= k 
        count={}
        left=0
        most_freq_char_count=0
        max_length=0

        for right in range(len(s)):
            # update char freq
            count[s[right]]=count.get(s[right],0)+1
            most_freq_char_count=max(most_freq_char_count,count[s[right]])
                
            while right - left +1 - most_freq_char_count >k: #while invalid
                # need to fix left
                count[s[left]]-=1
                left+=1
            max_length=max(max_length,right - left +1)

        return max_length

        