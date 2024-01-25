class Solution:
    def f(self,i,j,s1,s2,dp):
        if i==len(s1) or j==len(s2):
            return 0
        if (i,j) in dp:
            return dp[(i,j)]
        if s1[i]==s2[j]:
            dp[(i,j)]= 1+self.f(i+1,j+1,s1,s2,dp)
            return dp[(i,j)]
        else:
            dp[(i,j)]= max(self.f(i+1,j,s1,s2,dp),self.f(i,j+1,s1,s2,dp))
            return dp[(i,j)]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp={}
        return self.f(0,0,text1,text2,dp)