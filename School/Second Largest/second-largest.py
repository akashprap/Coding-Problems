#User function Template for python3
class Solution:
    
	def print2largest(self,arr, n):
		# code here
		largest=arr[0]
        second=0
		for i in arr:
		    if i>largest:
		        largest=i
		for i in arr:
		    if i!=largest and i>=second and i<largest:
		        second=i
		if second==0:
		    return -1
	    return second
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends