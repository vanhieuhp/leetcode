from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue = deque()        

    def ping(self, t: int) -> int:
        self.queue.append(t)

        # remove all times earlier than t - 3000
        while self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))     # Output: 1
print(obj.ping(100))   # Output: 2
print(obj.ping(3001))  # Output: 3
print(obj.ping(3002))  # Output: 3