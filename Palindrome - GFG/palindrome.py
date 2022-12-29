#User function Template for python3

class Solution:
	def is_palindrome(self, n):
		# Code here
		n=str(n)
		l=0
		h=len(str(n))-1
		while l<h:
		    if n[l]!=n[h]:
		        return "No"
		    else:
		        l+=1
		        h-=1
	    return "Yes"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_palindrome(n)
		print(ans)
# } Driver Code Ends