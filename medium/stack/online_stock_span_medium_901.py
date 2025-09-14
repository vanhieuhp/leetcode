class StockSpanner:

    def __init__(self):
        # stack holds pairs (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
sp = StockSpanner()
# param_1 = obj.next(price)
prices = [[],[28],[14],[28],[35],[46],[53],[66],[80],[87],[88]]
print([sp.next(p) for p in prices])