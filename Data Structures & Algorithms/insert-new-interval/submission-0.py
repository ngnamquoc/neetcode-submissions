class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        n=len(intervals)
        if n==0 or n==1:
            return intervals
        write=0
        for i in range(1,n):
            if intervals[i][0]<=intervals[write][1]:
                intervals[write][1]=max(intervals[write][1],intervals[i][1])
            else: #case no-overlapping
                write+=1
                intervals[write]=intervals[i]
        del intervals[write+1:]
        return intervals