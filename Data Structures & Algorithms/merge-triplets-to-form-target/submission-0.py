class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        filtered = []
        for triple in triplets:
            a,b,c = triple
            if a>target[0] or b>target[1] or c>target[2]:
                continue
            else:
                filtered.append(triple)

        res = [0,0,0]
        for a,b,c in filtered:
            res[0] = max(res[0], a)
            res[1] = max(res[1], b)
            res[2] = max(res[2], c)
        return res==target

            