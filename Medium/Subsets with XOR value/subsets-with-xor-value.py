#User function Template for python3
# import List
class Solution:
    def solve(self, arr, i, k, curr, dp):
        if i == 0:
            return curr == k
        if dp[i][curr] != -1:
            return dp[i][curr]
        taken = self.solve(arr, i-1, k, curr^arr[i-1], dp)
        nottake = self.solve(arr, i-1, k, curr, dp)
        dp[i][curr] = taken + nottake
        return dp[i][curr]

    def subsetXOR(self, arr, N, K):
        dp = [[-1]*(201) for i in range(N+1)]
        return self.solve(arr, N, K, 0, dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K = input().split()
        N = int(N)
        K = int(K)
        arr = input().split(' ')
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        print(ob.subsetXOR(arr,N,K))
# } Driver Code Ends