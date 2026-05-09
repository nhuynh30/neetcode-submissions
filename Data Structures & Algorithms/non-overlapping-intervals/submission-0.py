class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0

        intervals.sort(key=lambda x: x[1])
        lastEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start >= lastEnd:
                lastEnd = intervals[i][1]
            
            else:
                cnt+=1

        return cnt