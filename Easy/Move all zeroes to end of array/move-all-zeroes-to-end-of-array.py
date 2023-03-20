#User function Template for python3

class Solution:
	def pushZerosToEnd(self,nums, n):
    	# code here
    	j=0
        while j<len(nums):
            if nums[j]!=0:
                j+=1
            else:
                break
        for i in range(j+1,len(nums)):
            if nums[i]==0:
                continue
            else:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends