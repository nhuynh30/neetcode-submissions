class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lst = nums[:k]
        heapq.heapify(lst)
        for i in range(k,len(nums)):
            if nums[i]>lst[0]:
                heapq.heappop(lst)
                heapq.heappush(lst, nums[i])
        return lst[0]
        