class Solution:
    def f(self, n, dp):
        if n == 0:
            return 0
        if n in dp:
            return dp[n]
        
        min_squares = float('inf')
        num = 1
        while num * num <= n:
            min_squares = min(min_squares, 1 + self.f(n - num * num, dp))
            num += 1
        
        dp[n] = min_squares
        return min_squares

    def numSquares(self, n: int) -> int:
        dp = {}
        return self.f(n, dp)