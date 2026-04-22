import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            c = abs(heapq.heappop(heap))-abs(heapq.heappop(heap))
            heapq.heappush(heap, -1*c)
        return heap[0]*-1
