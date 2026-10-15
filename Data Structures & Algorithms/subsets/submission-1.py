class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #backtracking: choose,explore,undo
        #at every index, we make a decision (include or exclude)
        #index: which number we are deciding about
        #path: subset we built so far
        n=len(nums)
        path=[]
        result=[]
        def DFS(index:int)->None:
            #if we are out of range
            if index==n:
                result.append(path.copy())
                return
            #decide to include number
            path.append(nums[index])
            DFS(index+1)
            #undo inclusion, explore next
            path.pop()
            DFS(index+1)
        
        
        DFS(0)
        return result
        #time: O(2^n) * O(n) because every num has 2 choices and we need to copy the subset to result every time we are out range
        #auxiliary space (working memory): O(n) since we maintain path 

        
        