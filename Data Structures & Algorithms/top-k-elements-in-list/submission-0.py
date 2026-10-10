import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap=[]
        frequencies={}
        for num in nums:
            frequencies[num]=frequencies.get(num,0)+1

        for num, freq in frequencies.items():
            # push new candidate
            heapq.heappush(heap,(freq,num))
            # if became to large
            if len(heap)>k:
                # remove the smallest element
                heapq.heappop(heap)
        result=[]
        for freq,num in heap:
            result.append(num)
                

        return result


        