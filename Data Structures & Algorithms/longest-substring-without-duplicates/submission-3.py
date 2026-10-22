class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        last_seen={
           z:6,
           x:4, 
           y:5
        }
        longest_substring_length=0->1->2->3
             0123456
        s = "zxyzxyz"
                   r
                 l
        """
        n=len(s)
        if n==0:
            return 0

        left_pointer=0
        right_pointer=0
        longest_substring_length=0
        # need to track last seen index of duplicate char, then update left pointer to that index+1
        last_seen=dict() #char:last_seen_index
        while right_pointer<n:
            char=s[right_pointer]
            #check if duplication
            if char in last_seen and last_seen[char] >= left_pointer: #we need to check last_seen[char] >= left_pointer to ensure the duplication is within our window
                left_pointer=last_seen[char]+1
            #update last seen index
            last_seen[char]=right_pointer
            longest_substring_length=max(longest_substring_length,right_pointer-left_pointer+1)
            right_pointer+=1
          

        return longest_substring_length


        