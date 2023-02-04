#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
		if n==1:
		    return arr[0]
		dp=[[0]*2 for i in range(n)]
		dp[0][0]=0
		dp[0][1]=arr[0]
		for i in range(1,n):
		    dp[i][1]=dp[i-1][0]+arr[i]
		    dp[i][0]=max(dp[i-1][0],dp[i-1][1])
		return max(dp[n-1][0],dp[n-1][1])


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends