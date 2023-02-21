#User function Template for python3

class Solution:
    def minIteration(self, N, M, x, y):
        #code her
        d=0
        m=-99999999999999999999999999999999
        for i in range(N):
            for j in range(M):
                d=abs(i+1-x)+abs(j+1-y)
                m=max(d,m)
        return m
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N, M = map(int,input().split())
		x, y = map(int,input().split())
		ob = Solution()
		print(ob.minIteration(N, M, x, y))
# } Driver Code Ends