#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        l=0
        h=n-1
        while l<=h:
            mid=(l+h)//2
            prev = (mid-1+n)%n
            nex = (mid+1)%n
            if arr[mid]<=arr[prev] and arr[mid]<=arr[nex]:
              return mid
            elif arr[mid]<=arr[h]:
                h = mid-1
            else:
                l = mid+1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends