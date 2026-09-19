class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0)+1

        arr = [[] for _ in range(len(nums)+1)] 
        for key,val in freq.items():
            arr[val].append(key)

        ans = []
        
        for i in range(len(arr)-1, -1, -1):
            if k<=0:
                return ans
            if len(arr[i])>0:
                for j in range(len(arr[i])):
                    ans.append(arr[i][j])
                    k-=1
                    if k==0:
                        return ans

        return ans

        

        
        

