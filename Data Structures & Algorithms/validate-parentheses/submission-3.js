class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        // edge case
        if((s.length%2)!=0){
            return false
        }
        //dict
        let dict={
            "(":")",
            "[":"]",
            "{":"}",
        }
        let stack=[]

        for (let char of s){
            if (char=="(" || char=="[" || char=="{"){
                // push to stack, if opening bracket
                stack.push(char)

            }else{
                // pop from stack & compare
                if(dict[stack.pop()]!=char){
                    return false
                }
            }
            

        }
        return stack.length==0
  

    }
}
