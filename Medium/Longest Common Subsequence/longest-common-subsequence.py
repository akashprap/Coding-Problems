#User function Template for python
class Solution:
    def f(self,i,j,s1,s2,memo):
        if i<0 or j<0:
            return 0
        if (i,j) in memo:
            return memo[(i,j)]
        if s1[i]==s2[j]:
            memo[(i,j)]= 1+self.f(i-1,j-1,s1,s2,memo)
            return memo[(i,j)]
        else:
            memo[(i,j)]= max(self.f(i-1,j,s1,s2,memo),self.f(i,j-1,s1,s2,memo))
            return memo[(i,j)]
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        # memo={}
        # return self.f(x-1,y-1,s1,s2,memo)
        # code here
        dp=[[0]*(y+1) for i in range(x+1)]
        for i in range(x):
            for j in range(y):
                if s1[i]==s2[j]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        # print(dp)
        return dp[x-1][y-1]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends