#User function Template for python3
class Solution:
    def last_occur(self,arr,n,x):
        l=0
        h=n-1
        ans=-1
        while l<=h:
            mid=(l+h)//2
            if arr[mid]==x:
                ans=mid
                l=mid+1
            elif arr[mid]<x:
                l=mid+1
            else:
                h=mid-1
        return ans
    
    def first_occur(self,arr,n,x):
        l=0
        h=n-1
        ans=0
        while l<=h:
            mid=(l+h)//2
            if arr[mid]==x:
                ans=mid
                # l=mid+1
                h=mid-1
            elif arr[mid]<x:
                l=mid+1
            else:
                h=mid-1
        return ans
            
	def count(self,arr, n, x):
		# code herei
		if self.last_occur(arr,n,x)==-1:
		    return 0
		else:
		  #  print(self.last_occur(arr,n,x),self.first_occur(arr,n,x))
		    return self.last_occur(arr,n,x)-self.first_occur(arr,n,x)+1


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends