#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self,sr,sc,vis,grid,vec,sr0,sc0):
        n=len(grid)
        m=len(grid[0])
        vis[sr][sc]=1
        vec.append((sr-sr0,sc-sc0))
        dr=[-1,0,1,0]
        dc=[0,-1,0,1]
        for i in range(4):
            nr=sr+dr[i]
            nc=sc+dc[i]
            if nr>=0 and nr<n and nc>=0 and nc<m and vis[nr][nc]==0 and grid[nr][nc]==1:
                self.dfs(nr,nc,vis,grid,vec,sr0,sc0)
        
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        n=len(grid)
        m=len(grid[0])
        ss=set()
        vis=[[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if vis[i][j]==0 and grid[i][j]==1:
                    vec=[]
                    self.dfs(i,j,vis,grid,vec,i,j)
                    # print(vec)
                    ss.add(tuple(vec))
        return len(ss)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends