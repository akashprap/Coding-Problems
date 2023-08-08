#User function Template for python3
from collections import defaultdict
from math import gcd
class Solution:
    def countFractions(self, n, num, den):
        # Your code here
        mapp=defaultdict(int)
        ans=0
        for a,b in zip(num,den):
            gc=gcd(a,b)
            a=a//gc
            b=b//gc
            ans+=mapp[(b-a,b)]
            mapp[(a,b)]+=1
        return ans
        


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    numerator = list(map(int,input().split()))
    denominator = list(map(int,input().split()))
    ob = Solution()
    print(ob.countFractions(n,numerator,denominator))
# } Driver Code Ends