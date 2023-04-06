#User function Template for python3
mod=10**9+7
class Solution:
    def nCr(self, n, r):
        if r > n:
            return 0
        nu,de= 1, 1
        for i in range(r):
            nu = (nu * (n-i)) % mod
            de = (de * (i+1)) % mod
        de_in = pow(de, mod-2, mod)
        return (nu * de_in) % mod



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