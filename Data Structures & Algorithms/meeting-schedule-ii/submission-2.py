"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)<=1:
            return len(intervals)
        
        heap = []
        intervals.sort(key= lambda x: x.start)
        time = 0
        res = 0

        for i in range(len(intervals)):
            curr = intervals[i]
            time = curr.start
            if i==0:
                heapq.heappush(heap, curr.end)
                res=1
                continue
            while heap and time >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, curr.end)
            res = max (res, len(heap))

        return res


            
        
            

