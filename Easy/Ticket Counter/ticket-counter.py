from collections import deque
from math import ceil,floor
class Solution:
    def distributeTicket(self, N: int, K: int) -> int:
        x=(ceil((float)(N+K+1)/(2*K*1.0)))-1
        if(x*K+((x-1)*K)==N):
            return x*K
        elif(N-(x*K+((x-1)*K))<=K):
            return x*K+1
        return N-(x*K)


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    
    N, K = map(int, input().split())
    
    obj = Solution()
    res = obj.distributeTicket(N, K)
    
    print(res)
# } Driver Code Ends