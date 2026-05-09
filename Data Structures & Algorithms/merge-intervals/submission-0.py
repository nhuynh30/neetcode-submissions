class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []

        for i in range(len(intervals)):
            #merged is empty or current interval start > merged last interval end (no overlap)
            if not merged or intervals[i][0]>merged[-1][1]:
                merged.append(intervals[i])

            #since we sort by start, start in merged is always less than or equal already
            #no need to update start -> only update end time (merging 2 intervals)
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            
        return merged