class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        self.dic = {}



    def get(self, key: int) -> int:
        node = self.dic.get(key,-1)
        if node == -1:
            return -1
        self.dequeue(node)
        self.enqueue(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        node = Node(key,value)
        if key in self.dic:
            self.dequeue(self.dic[key])
            self.enqueue(node)
            self.dic[key] = node

        else:
            if len(self.dic)<self.cap:
                self.dic[key] = node
                self.enqueue(node)

            else:
                remove = self.head.next
                self.dequeue(remove)
                del self.dic[remove.key]
                self.dic[key] = node
                self.enqueue(node)

                





    def enqueue(self,node):
        prevNode = self.tail.prev
        prevNode.next = node
        node.prev = prevNode

        self.tail.prev = node
        node.next = self.tail




    def dequeue(self,node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode




        
