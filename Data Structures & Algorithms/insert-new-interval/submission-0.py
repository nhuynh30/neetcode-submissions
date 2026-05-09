class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            curr = intervals[i]

            #Case1 : newInterval is after the current interval
            if newInterval[0]>curr[1]:
                res.append(curr)


            #Case2: newInterval is before the current interval -> merge to ans
            elif newInterval[1] < curr[0]:
                res.append(newInterval)
                return res + intervals[i:]

            #Case3 : Overlap ->mergen them into newInterval
            else:
                newInterval[0] = min(newInterval[0], curr[0])
                newInterval[1] = max(newInterval[1], curr[1])
        
        res.append(newInterval)

        return res




            



