class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for word in strs:
            count=[0]*26 #26 alphabets, index 0 corresponds to "a"
            for char in word:
                index=ord(char)-ord("a")
                count[index]+=1 #increament by 1
            # convert to tuple to be used as key in dict
            key=tuple(count)
            if key in groups:
                groups[key].append(word)
            else:
                groups[key]=[word]
        return list(groups.values())
        