class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        last = None
        cnt =0
        for start, end in intervals:
            if last is None:
                last = end
            
            elif start < last:
                cnt+=1
            
            else:
                last = end

        return cnt
                
