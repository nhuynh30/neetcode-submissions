class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(enque, process, index) for index, (enque, process) in enumerate(tasks)]
        heapq.heapify(tasks)
        available = []
        t = 0
        res = []
        while tasks or available:
            if not available and t<tasks[0][0]:
                t = tasks[0][0]
            
            while tasks and tasks[0][0]<=t:
                enque, process, i = heapq.heappop(tasks)
                heapq.heappush(available, (process, i))
                

            if available:
                enque, i = heapq.heappop(available)
                res.append(i)
                t+= enque


        return res
