class SeatManager:

    def __init__(self, n: int):
        self.heap=[i for i in range(1,n+1)]
        heapq.heapify(self.heap)
        # self.ss=set()

    def reserve(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)

        

    def unreserve(self, sn: int) -> None:
        heapq.heappush(self.heap,sn)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)