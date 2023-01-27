#User function Template for python3

class Solution:
    def f(self,ind,st,c,path):
        if ind==len(st):
            return 1
        if path[ind]!=-1:
            return path[ind]
        one,two=0,0
        if int(st[ind])>=1 and int(st[ind])<=9:
            one=self.f(ind+1,st,c,path)
        temp=st[ind:ind+2]
        if ind<c-1 and 10<=int(temp)<=26:
            two=self.f(ind+2,st,c,path)
        path[ind]=(one+two)%(1000000007)
        return path[ind]
	def CountWays(self, st):
		# Code here
		path=[-1]*len(st)
		c=len(st)
		return self.f(0,st,c,path)
		#print(path)
		#return path[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.CountWays(str)
		print(ans)

# } Driver Code Ends