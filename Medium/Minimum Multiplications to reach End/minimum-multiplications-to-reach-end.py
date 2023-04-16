#User function Template for python3

from typing import List
from collections import deque
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        mod=100000
        dist=[float("inf") for i in range(mod)]
        dist[start]=0
        q=deque()
        q.append((0,start))
        while q:
            step,node=q.popleft()
            if node==end:
                return step
            for adj in arr:
                newnode=(node*adj)%mod
                if step+1<dist[newnode]:
                    dist[newnode]=1+step
                    q.append((step+1,newnode))
        return -1
                
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends