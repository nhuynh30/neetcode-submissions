class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for start,end in intervals:
            if not merged:
                merged.append([start,end])
            elif start <= merged[-1][1]:
                merged[-1][1] = max(end,merged[-1][1])
            else:
                merged.append([start,end])

        
        return merged
            

            