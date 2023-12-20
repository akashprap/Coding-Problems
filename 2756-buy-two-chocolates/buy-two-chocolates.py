class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapify(prices)
        a=heappop(prices)
        b=heappop(prices)
        if a+b>money:
            return money
        else:
            return money-(a+b)
        