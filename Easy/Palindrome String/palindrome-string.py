#User function Template for python3
class Solution:
	def isPalindrome(self, S):
	    z=S
	    if S==z[::-1]:
	        return 1
	    return 0
# 		# code here
# 		def ispal(i,j,S):
# 		    if i>=j:
# 		        return 1
# 		    if S[i]!=S[j]:
# 		        return 0
# 		    return ispal(i+1,j-1,S)
# 	    return ispal(0,len(S)-1,S)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends