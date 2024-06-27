import queue
class MyQueue:

    def __init__(self):
        self.s1 = queue.LifoQueue()
        self.s2 = queue.LifoQueue()
        
    def push(self, x: int) -> None:
        while not self.s1.empty():
            item = self.s1.get()
            self.s2.put(item)
        self.s1.put(x)
        while not self.s2.empty():
            item = self.s2.get()
            self.s1.put(item)

    def pop(self) -> int:
        return self.s1.get()
        

    def peek(self) -> int:
        item = self.s1.get()
        self.s1.put(item)
        return item

    def empty(self) -> bool:
        return self.s1.qsize() == 0        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()