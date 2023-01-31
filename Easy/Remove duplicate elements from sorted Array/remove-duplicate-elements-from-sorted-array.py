#User function template for Python

class Solution:	
	def remove_duplicate(self, nums, N):
		# code here
		k=len(set(nums))
        f=nums[0]
        ind=0
        for i in range(len(nums)):
            if nums[i]==f:
                continue
            else:
                nums[ind]=f
                f=nums[i]
                ind+=1
        nums[ind]=f
        return k


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends