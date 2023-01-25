#User function Template for python3
class Solution:
    def f(self,ind,sumi,arr,ans):
        if ind>=len(arr):
            ans.append(sumi)
            return
        take=self.f(ind+1,sumi+arr[ind],arr,ans)
        
        nottake=self.f(ind+1,sumi,arr,ans)
            
	def subsetSums(self, arr, N):
		# code here
		ans=[]
		s=0
		self.f(0,0,arr,ans)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends