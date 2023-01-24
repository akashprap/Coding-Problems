#User function Template for python3
from collections import defaultdict
class Solution:

	def convert(self,arr, n):
		# code here
		array=defaultdict(int)
		for i in range(n):
		    array[arr[i]]=i
		ans=arr.copy()
		ans.sort()
		for i in range(n):
		    ind=array[ans[i]]
		    arr[ind]=i
		return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.convert(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends