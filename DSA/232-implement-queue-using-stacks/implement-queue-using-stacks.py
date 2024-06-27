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
        print("s1",self.s1.queue,"\n","s2", self.s2.queue)

    def pop(self) -> int:
        print("s1",self.s1.queue,"\n","s2", self.s2.queue)
        return self.s1.get()
        # if self.s1.qsize()> 1:
        #     self.s2.put(self.s1.get())
        # print("s1",self.s1.queue,"\n","s2", self.s2.queue)
        # pop_el = self.s1.get()
        # print("s1",self.s1.queue,"\n","s2", self.s2.queue)
        # self.s2, self.s1 = self.s1, self.s2
        # return pop_el

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