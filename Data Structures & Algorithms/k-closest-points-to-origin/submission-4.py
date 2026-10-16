import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calculate the distance between every point to (0,0)
        min_heap=[]
        result=[]
        for x,y in points: #T1=O(nlogn)
            distance=x**2+y**2 #don't need sqrt as the distance are proportionally similar
            heapq.heappush(min_heap,(distance,x,y)) #by default, use the 1st element to compare
        for i in range(k): #T2=O(klogn)
            distance,x,y=heapq.heappop(min_heap)
            print(distance)
            result.append([x,y])
        return result
        #time: O(nlogn)
        #space:O(n)
        
        