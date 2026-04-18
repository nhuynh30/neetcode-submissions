class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None



class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            self.cache[key].val = value
            self.delete(node)
            self.insert(self.cache[key])
        else:
            self.cache[key] = Node(key,value)
            if (len(self.cache)>self.capacity):
                node = self.head.next
                self.delete(node)
                del self.cache[node.key]
            self.insert(self.cache[key])


    def delete(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self,node):
        prev = self.tail.prev
        node.prev=prev
        prev.next = node
        node.next = self.tail
        self.tail.prev = node
        
        