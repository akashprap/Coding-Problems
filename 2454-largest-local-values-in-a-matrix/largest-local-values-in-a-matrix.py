class Solution:
    def maxval(self,i,j,grid):
        n=len(grid)
        m=len(grid[0])
        maxx=0
        for r in range(i,i+3):
            for c in range(j,j+3):
                maxx=max(maxx,grid[r][c])
        return maxx

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        maxLocal = [[0]*(m-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(m-2):
                maxLocal[i][j]=self.maxval(i,j,grid)
        return maxLocal
