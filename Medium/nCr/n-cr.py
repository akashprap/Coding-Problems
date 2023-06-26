#User function Template for python3
class Solution:
    def nCr(self, n, r):
        MOD = int(1e9) + 7

        dp = [[0] * (r + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, min(i, r) + 1):
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % MOD

        return dp[n][r]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends