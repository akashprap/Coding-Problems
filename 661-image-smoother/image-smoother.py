class Solution:
    def visit(self,i,j,n,m,img):
        diff=[[0,0],[-1,0],[1,0],[-1,1],[0,1],[0,-1],[-1,-1],[1,1],[1,-1]]
        ans=0
        c=0
        for dr,dc in diff:
            nr=i+dr
            nc=j+dc
            if nr>=0 and nr<n and nc>=0 and nc<m:
                c+=1
                ans+=img[nr][nc]
        return ans//c
            
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n=len(img)
        m=len(img[0])
        ans=[[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j]=self.visit(i,j,n,m,img)
        return ans
        