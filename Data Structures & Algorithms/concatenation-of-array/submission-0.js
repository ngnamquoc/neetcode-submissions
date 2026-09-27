class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        //initialize dynamic ar
        const n=nums.length;
        let ans=[];
        let i=0;
        while(i<n){
            ans[i]=nums[i]
            ans[i+n]=nums[i]
            i++;
        }
        return ans;
    }
}
