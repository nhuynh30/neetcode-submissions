class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if len(self.stack)<1:
            self.stack.append((price,1))
            return 1
        cnt = 1
        while self.stack and self.stack[-1][0]<=price:
            x, y = self.stack.pop()
            cnt+=y
        
        self.stack.append((price,cnt))
        
        return cnt
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)