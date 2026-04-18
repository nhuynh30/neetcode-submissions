class TimeMap:


    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((value, timestamp))
        else:
            self.dic[key] = [(value, timestamp)]
    

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        value = self.dic[key]
        l = 0
        r = len(value)-1
        res = -1
        while(l<=r):
            mid = l+(r-l)//2
            if value[mid][1] == timestamp:
                return value[mid][0]
            elif value[mid][1] < timestamp:
                res = mid
                l=mid+1
            else:
                r=mid-1
        return value[res][0] if res !=-1 else ""

        
        
