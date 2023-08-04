#User function Template for python3

from typing import List
import sys

sys.setrecursionlimit(10**6)

class Solution:
    def reverse(self,St): 
        #code here
        ans=[]
        def f(ind):
            if ind<0:
                return 
            ans.append(St[ind])
            f(ind-1)
        f(len(St)-1)
        St[:]=ans


#{ 
 # Driver Code Starts

#Initial Template for Python 3

 
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
# } Driver Code Ends