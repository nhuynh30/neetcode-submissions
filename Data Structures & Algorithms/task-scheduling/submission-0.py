from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        for task in tasks:
            dic[task] = dic.get(task,0)+1

        lst = []
        for i in dic:
            heapq.heappush(lst, (-dic[i], i))
        
        t = 0
        queue = deque()


        while lst or queue:
            t+=1
            if queue and queue[0][0]<=t:
                _ , x, y = queue.popleft()
                heapq.heappush(lst, (x, y))
            if not lst:
                continue
            freq, task = heapq.heappop(lst)
            freq+=1
            if freq < 0:
                queue.append((t+n+1,freq,task))

        return t
            
            



