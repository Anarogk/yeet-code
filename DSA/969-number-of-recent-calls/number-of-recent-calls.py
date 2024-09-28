from collections import deque
class RecentCounter:

    def __init__(self):
        self.counter: int = 0
        self.queue = deque()

    def ping(self, t: int) -> int:
        start = max(0, t-3000)
        self.queue.append(t)
        if self.queue:
            while self.queue[0]< start:
                self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)