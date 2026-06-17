class MyCircularQueue:

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [-1] * k
        self.front = 0
        self.back = -1
        self.k = k
        self.size = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        
        self.back=(self.back+1)%self.k
        self.queue[self.back] = value
        self.size+=1

        return True

        
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.size==0:
            return False
        self.size-=1
        val = self.queue[self.front]
        self.front = (self.front+1)%self.k
        return True
        

    def Front(self):
        """
        :rtype: int
        """
        if self.size==0:
            return -1
        return self.queue[self.front]

    def Rear(self):
        """
        :rtype: int
        """
        if self.size==0:
            return -1
        return self.queue[self.back]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size==0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()