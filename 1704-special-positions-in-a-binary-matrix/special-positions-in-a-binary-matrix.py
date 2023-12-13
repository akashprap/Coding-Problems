class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        row=[0]*n
        col=[0]*m
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    row[i]+=1
                    col[j]+=1
        # print(row,col)
        ans=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    if row[i]==1 and col[j]==1:
                        ans+=1
        return ans
