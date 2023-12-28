class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        def calculatelen(cnt):         #length calculator
            if cnt==0: return 0
            elif cnt==1: return 1
            elif cnt < 10: return 2
            elif cnt < 100: return 3
            else: return 4
        
        
        n = len(s)
        x = 999999
        dp = [[x]*(k+1) for i in range(n+1)]
        for i in range(k+1):
            dp[0][i] = 0

        for i in range(1,n+1):
            for j in range(k+1):
                
                cnt,remove = 0,0
                
                if j > 0: dp[i][j] = dp[i-1][j-1]
                    
                for p in range(i,0,-1):
                    if(s[p-1] == s[i-1]): cnt+=1
                    else: 
                        remove += 1
                        if remove > j: break
                    dp[i][j] = min(dp[i][j],(dp[p-1][j-remove] + calculatelen(cnt)))
                    
        return dp[n][k]