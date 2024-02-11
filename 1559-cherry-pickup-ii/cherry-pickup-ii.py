class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dp={}
        def dfs(r,c1,c2,dp):
            if c1==c2 or min(c1,c2)<0 or max(c1,c2)>=cols:
                return 0
            if r==rows-1:
                return grid[r][c1]+grid[r][c2]
            if (r,c1,c2) in dp:
                return dp[(r,c1,c2)]
            res=0
            for d_c1 in [-1,0,1]:
                for d_c2 in [-1,0,1]:
                    res=max(res,dfs(r+1,c1+d_c1,c2+d_c2,dp))
            res+=grid[r][c1]+grid[r][c2]
            dp[(r,c1,c2)]=res
            return dp[(r,c1,c2)]
            # return res
        return dfs(0,0,cols-1,dp)
