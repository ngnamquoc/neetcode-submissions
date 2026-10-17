class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #similar to meeting rooms schedule problem
        #just to certain we sort the intervals by start 
        
        n=len(intervals)
        if n==0 or n==1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        write=0
        for i in range(1,n):
            if intervals[i][0] <= intervals[write][1]: #case overlapping -> merge
                intervals[write][1]=max(intervals[write][1],intervals[i][1])
            else: #case no-overlapping, move i to write+1 position
                write+=1
                intervals[write]=intervals[i]
        #remove tail
        del intervals[write+1:]


        return intervals
        #time: O(n)
        #space: O(n)




        