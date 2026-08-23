class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        res = []
        bucket = [[] for _ in range(len(nums)+1)]
        for num in nums:
            dic[num] = dic.get(num, 0)+1

        for num, count in dic.items():
            bucket[count].append(num)

        for i in range(len(nums), -1, -1):
            if bucket[i]:
                for num in bucket[i]:
                    res.append(num)
                    if(len(res)==k):
                        return res
            
        
        


