class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False

        # dict
        dict={
            "(":")",
            "[":"]",
            "{":"}"
        }

        stack=[]

        for char in s:
            # case opening bracket
            if char=="(" or char=="[" or char=="{":
                stack.append(char)
            else:
                if len(stack)==0 or char != dict[stack.pop()]:
                    return False
            
        return len(stack)==0



        