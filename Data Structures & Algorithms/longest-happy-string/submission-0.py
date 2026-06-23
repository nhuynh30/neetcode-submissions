class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr = []
        if a>0:
            heapq.heappush(arr, (-a, 'a'))
        if b>0:
            heapq.heappush(arr, (-b, 'b'))
        if c>0:
            heapq.heappush(arr, (-c, 'c'))

        res = ''
        letter = ''

        while arr:
            letter = arr[0][1]
            if not (len(res) >= 2 and res[-1] == letter and res[-2] == letter):
                num, letter = heapq.heappop(arr)
                res += letter
                num+=1
                if num<0:
                    heapq.heappush(arr, (num, letter))
                
            else:
                pop = heapq.heappop(arr)
                if not arr:
                    return res
                num, letter = heapq.heappop(arr)
                res += letter
                num+=1
                if num<0:
                    heapq.heappush(arr, (num, letter))
                heapq.heappush(arr, pop)

        return res