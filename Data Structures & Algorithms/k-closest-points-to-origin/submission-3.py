class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return math.sqrt(math.pow(x, 2) + math.pow(y,2))

        heap = []

        for x,y in points:
            z = distance(x,y)
            heapq.heappush(heap, (-z, (x,y)))
            while len(heap)>k:
                heapq.heappop(heap)

        ans = []
        for z, pair in heap:
            x,y, = pair
            ans.append([x,y])

        return ans
