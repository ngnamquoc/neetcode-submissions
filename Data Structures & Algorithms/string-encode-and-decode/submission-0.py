class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str=""
        for word in strs: 
            mark=str(len(word))+"#"
            encoded_str+=mark+word

        return encoded_str



    def decode(self, s: str) -> List[str]:
        strs=[]
        n=len(s) #n=20
        i=0
        while i<n: 
            j=i
            while(s[j]!="#"):
                j+=1
            length=int(s[i:j])
            word=s[j+1:j+1+length]
            strs.append(word)
            i=j+1+len(word)
            
        return strs
