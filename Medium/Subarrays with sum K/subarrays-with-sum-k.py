#User function Template for python3
from collections import defaultdict
class Solution:
    def findSubArraySum(self, Arr, N, k):
        # code here
        mappy=defaultdict(int)
        ans=0
        cursum=0
        for i in range(N):
            cursum+=Arr[i]
            if cursum==k:
                ans+=1
            if cursum-k in mappy:
                ans+=mappy[cursum-k]
            mappy[cursum]+=1
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.findSubArraySum(Arr, N, k))
# } Driver Code Ends