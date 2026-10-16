class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #1st approach: backtracking
        #possible key word -> thinking of backtracking problem: decide,explore,backtrack (undo)
        #permutations means arranging elements in every possible order. Mathematically represented by n!
        # can tell num of permutations from n=len(nums): 
        #for i in range(n):
        #   permutations*=n-i
        # path=[]
        # result=[]
        # n=len(nums)
        # def DFS():
        #     if len(path)==n:
        #         result.append(path.copy())
        #     for num in nums:
        #         if num in path:
        #             continue
        #         path.append(num)
        #         DFS()
        #         path.pop()
        
        # DFS()
        # return result
        # time complexity: O(n*n!)
        #auxiliary space: O(n)
        #total space: O(n*n!)

        #2nd approach: iterative insertions
        result=[[]]
        
        for num in nums:
            new_permutations=[]
            for perm in result:
                # insert num to perm, then append to new_permutations
                for i in range(len(perm)+1):
                    new_permutations.append(perm[:i]+[num]+perm[i:])
            result=new_permutations
        return result



