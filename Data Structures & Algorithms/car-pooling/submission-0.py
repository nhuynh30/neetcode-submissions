class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = [(pickup, dropoff, numpass) for numpass, pickup, dropoff in trips]
        heapq.heapify(trips)

        current = 0
        t = 0
        onBoard = []

        while trips:
            pickup, dropoff, numpass = heapq.heappop(trips)
            if t<pickup:
                t=pickup

            while onBoard and onBoard[0][0]<=t:
                dis, removed = heapq.heappop(onBoard)
                current -= removed

            if current+numpass>capacity:
                return False

            current += numpass
            heapq.heappush(onBoard, (dropoff, numpass))

        
        return True

            
            