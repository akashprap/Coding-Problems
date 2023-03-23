#User function Template for python3
import sys
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self,r,c,grid,vis):
        n=len(grid)
        m=len(grid[0])
        vis[r][c]=1
        dr=[-1,-1,0,1,1,1,0,-1]
        dc=[0,1,1,1,0,-1,-1,-1]
        for i in range(8):
            nr=r+dr[i]
            nc=c+dc[i]
            if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]==1 and vis[nr][nc]==0:
                self.dfs(nr,nc,grid,vis)
    def numIslands(self, grid):
        n=len(grid)
        m=len(grid[0])
        visited=[[0]*m for i in range(n)]
        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not visited[i][j]:
                    ans+=1
                    self.dfs(i,j,grid,visited)
        return ans


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
        print(obj.numIslands(grid))
# } Driver Code Ends