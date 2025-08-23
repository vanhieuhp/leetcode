import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.min_heap = [1]
        heapq.heapify(self.min_heap)

    def popSmallest(self) -> int:
        if len(self.min_heap) == 1:
            self.current += 1
            heapq.heappush(self.min_heap, self.current)
        
        return heapq.heappop(self.min_heap)

    def addBack(self, num: int) -> None:
        if num >= self.current or num in self.min_heap:
            return
        
        heapq.heappush(self.min_heap, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
print(obj.popSmallest())  # 1
obj.addBack(1)
obj.addBack(1)
param_1 = obj.popSmallest()
# obj.addBack(num)