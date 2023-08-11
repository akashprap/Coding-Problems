#User function Template for python3

class Solution:
    def f(self,ind,coins,sm,dp):
        if ind==0:
            return 1 if sm%coins[ind]==0 else 0
        if sm<=0:
            return 1
        if (ind,sm) in dp:
            return dp[(ind,sm)]
        take=0
        nottake=0
        if sm>=coins[ind]:
            take=self.f(ind,coins,sm-coins[ind],dp)
        nottake=self.f(ind-1,coins,sm,dp)
        dp[(ind,sm)]= take+nottake
        return dp[(ind,sm)]
        
        
    def count(self, coins, n, amount):
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for j in range(1, amount + 1):
                if coins[i] > j:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - coins[i]]

        return dp[0][amount]
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends