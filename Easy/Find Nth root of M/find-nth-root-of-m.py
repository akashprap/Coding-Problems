#User function Template for python3

class Solution:
	def NthRoot(self, n, m):
		# Code here
		l=1
		h=m
		ans=1
		while l<=h:
		    mid=(l+h)//2
		    if mid**n==m:
		        ans=mid
		        return ans
		    elif mid**n<m:
		        l=mid+1
		    else:
		        h=mid-1
	    return -1
		  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends