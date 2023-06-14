#User function Template for python3
import heapq as hq
class Solution:
    def maxDiamonds(self, A, N, k):
        # code here 
        heap=[]
        hq.heapify(heap)
        for i in A:
            hq.heappush(heap,-i)
        ans=0
        while k:
            temp=-hq.heappop(heap)
            hq.heappush(heap,-(temp//2))
            ans+=temp
            k-=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxDiamonds(A,N,K))
# } Driver Code Ends