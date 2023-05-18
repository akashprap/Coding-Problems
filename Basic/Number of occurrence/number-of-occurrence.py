#User function Template for python3
class Solution:
    def bin_search(self,flag,l,r,nums,target):
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
            else:
                ans=mid
                if flag:
                    r=mid-1
                else:
                    l=mid+1
        return ans

	def count(self,nums, n, target):
		# code here
		l=0
        r=len(nums)-1
        left=self.bin_search(True,l,r,nums,target)
        right=self.bin_search(False,l,r,nums,target)
        if left==-1 and right==-1:
            return 0
        return right-left+1


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