
from typing import List


class Solution:
        
    def stockBuyAndSell(self, n : int, prices : List[int]) -> int:
        def maxProfit(prices: List[int]) -> int:
            profit=0
            for i in range(1,len(prices)):
                if prices[i]>prices[i-1]:
                    profit+=prices[i]-prices[i-1]
            return profit
        return maxProfit(prices)


#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        prices=IntArray().Input(n)
        
        obj = Solution()
        res = obj.stockBuyAndSell(n, prices)
        
        print(res)
        

# } Driver Code Ends