#User function Template for python3
from collections import deque
class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        vis=[[0]*M for i in range(N)]
        q=deque()
        if A[0][0]==0:
            return -1
        q.append((0,0,0))
        while q:
            row,col,step=q.popleft()
            if row==X and col==Y:
                return step
            else:
                for dr,dc in [[-1,0],[0,1],[1,0],[0,-1]]:
                    nr=row+dr
                    nc=col+dc
                    if nr>=0 and nr<N and nc>=0 and nc<M and A[nr][nc]==1 and not vis[nr][nc]:
                        vis[nr][nc]=1
                        q.append((nr,nc,step+1))
        return -1


#{ 
 # Driver Code Starts

#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
# } Driver Code Ends