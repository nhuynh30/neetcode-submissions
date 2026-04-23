class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return math.sqrt((x**2)+(y**2))
        
        dic = {}
        calculated = [0] * len(points)
        for i in range(len(points)):
            x= -1* distance(points[i][0], points[i][1])
            calculated[i] = x
            if x in dic:
                dic[x].append(i)
            else:
                dic[x] = [i]

        lst = calculated[:k]
        heapq.heapify(lst)
        for i in range(k, len(calculated)):
            if calculated[i] > lst[0]:
                heapq.heappop(lst)
                heapq.heappush(lst, calculated[i])
        res = []
        for x in lst:
            i = dic[x].pop()
            res.append(points[i])
        
        return res










