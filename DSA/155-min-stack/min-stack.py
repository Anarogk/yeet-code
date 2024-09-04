class MinStack:

    def __init__(self):
        self.arr = [] # main arr
        self.minStack = [] # maintaining minStack

    def push(self, val: int) -> None:
        self.arr.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.arr.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()