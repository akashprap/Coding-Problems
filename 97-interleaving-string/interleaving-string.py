class Solution:
    def f(self,i,j,s1,s2,s3,dp):
        if i==len(s1) and j==len(s2):
            return True
        if (i,j) in dp:
            return dp[(i,j)]
        if i<len(s1) and s1[i]==s3[i+j] and self.f(i+1,j,s1,s2,s3,dp):
            return True
        if j<len(s2) and s2[j]==s3[i+j] and self.f(i,j+1,s1,s2,s3,dp):
            return True
        dp[(i,j)]=False
        return dp[(i,j)]
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        dp={}
        return self.f(0,0,s1,s2,s3,dp)