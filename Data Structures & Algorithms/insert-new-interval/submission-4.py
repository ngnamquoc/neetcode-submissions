class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # optimization, try to inset new Interval without re-sorting:
        #best is it greater than the last element in intervals
        if not intervals:
            return [newInterval]
        if newInterval[0]>=intervals[-1][0]:
            intervals.append(newInterval)
        else:
            for i,(start,end) in enumerate(intervals):
                if newInterval[0]<=start:
                    #insert before
                    intervals.insert(i,newInterval)
                    break


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

        #time: O(n)
        #auxiliary space: O(1)