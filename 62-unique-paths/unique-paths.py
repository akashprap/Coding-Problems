class Solution:
    def uniquePaths(self, n: int, m: int) -> int:
        vis=[[0]*(m+1) for i in range(n+1)]
        @cache
        def f(i,j):
            if i==n-1 and j==m-1:
                return 1
            vis[i][j]=1
            ans=0
            for dr,dc in [[1,0],[0,1]]:
                nr=i+dr
                nc=j+dc
                if nr>=0 and nr<n and nc>=0 and nc<m and not vis[nr][nc]:
                    ans+=f(nr,nc)
            vis[i][j]=0
            return ans
        return f(0,0)