#User function Template for python3

import heapq as hq
class Solution:
    def minimizeSum(self, N, arr):
        # Code here
        ans=0
        heap=[]
        hq.heapify(heap)
        for i in arr:
            hq.heappush(heap,i)
        while len(heap)>=2:
            a=hq.heappop(heap)
            b=hq.heappop(heap)
            ans+=(a+b)
            hq.heappush(heap,(a+b))
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minimizeSum(n, A))
# } Driver Code Ends