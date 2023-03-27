#User function Template for python3

class Solution:
    def sort012(self,nums,n):
        l=0
        mid=0
        high=n-1
        while mid<=high:
            if nums[mid]==0:
                nums[l],nums[mid]=nums[mid],nums[l]
                l+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends