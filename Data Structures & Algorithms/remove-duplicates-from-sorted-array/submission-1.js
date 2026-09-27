class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        if(nums.length==1) return nums.length
        // remove duplicate
        let unique=Array.from(new Set(nums));
        // sort
        unique=unique.sort((a,b)=>a-b);
        // update the original nums
        for(let i=0;i<unique.length;i++){
            nums[i]=unique[i];
        }
        return unique.length

    }
}
