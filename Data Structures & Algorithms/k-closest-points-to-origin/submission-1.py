import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calculate the distance between every point to (0,0)
        min_heap=[]
        result=[]
        for x,y in points:
            distance=math.sqrt((x-0)**2+(y-0)**2)
            heapq.heappush(min_heap,(distance,x,y)) #by default, use the 1st element to compare
        for i in range(k):
            distance,x,y=heapq.heappop(min_heap)
            print(distance)
            result.append([x,y])
        return result
        
        