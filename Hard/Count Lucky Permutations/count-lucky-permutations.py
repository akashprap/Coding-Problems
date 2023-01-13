#User function Template for python3
from collections import defaultdict
class Solution: 
    def luckyPermutations(self, N, M, arr, graph):
        ind = defaultdict(list)
        for i, a in enumerate(arr):
            ind[a].append(i)
            
        dp = [[0 for j in range(1<<N)] for i in range(N)]
        for i in range(N):
            dp[i][1<<i] = 1

        for mask in range(1, 1<<N):
            for u, v in graph:
                for i in ind[u]:
                    for j in ind[v]:
                        if mask&(1<<i) and mask&(1<<j):
                            maski, maskj = mask ^ (1<<i), mask ^ (1<<j)
                            dp[i][mask] += dp[j][maski]
                            dp[j][mask] += dp[i][maskj]

        return sum(dp[i][(1<<N) - 1] for i in range(N))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0:
        N, M=[int(i) for i in input().split()]
        arr = [int(i) for i in input().split()]
        graph = []
        for i in range(M):
            graph.append([int(i) for i in input().split()])
        ob = Solution()
        print(ob.luckyPermutations(N, M, arr,graph))
        
        T -= 1
# } Driver Code Ends