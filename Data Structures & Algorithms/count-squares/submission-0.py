class CountSquares:

    def __init__(self):
        self.map = {}

    def add(self, point: List[int]) -> None:
        x,y = point
        self.map[(x,y)] = self.map.get((x,y), 0)+1


    def count(self, point: List[int]) -> int:
        res = 0
        for x,y in self.map.keys():
            if x==point[0]:
                side = abs(y-point[1])
                if side==0:
                    continue
                if (x-side, point[1]) in self.map and (x-side, y) in self.map:
                    res+= (self.map[(x-side, point[1])] * self.map[(x-side, y)]) * self.map[(x,y)]

                if (x+side, point[1]) in self.map and (x+side, y) in self.map:
                    res+= (self.map[(x+side, point[1])] * self.map[(x+side, y)]) * self.map[(x,y)] 
            
        return res

                

