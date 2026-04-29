from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        for task in tasks:
            dic[task] = dic.get(task, 0)+1
        
        lst = []
        for i in dic:
            heapq.heappush(lst, (-dic[i], i))
        queue = deque()

        t = 0
        while lst or queue:
            if not lst:
                t=queue[0][0]

            if queue and queue[0][0]<=t:
                _,x, y = queue.popleft()
                heapq.heappush(lst, (x,y))

            t+=1
            freq, val = heapq.heappop(lst)
            freq+=1
            if freq<0:
                queue.append((t+n, freq, val))


        return t
