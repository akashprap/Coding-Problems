#User function Template for python3
class Solution:

	def maxIndexDiff(self,arr,n):
		#code here
		pref=[arr[0]]*n
		suff=[arr[-1]]*n
		for i in range(1,n):
		    pref[i]=min(pref[i-1],arr[i])
		for j in range(n-2,-1,-1):
		    suff[j]=max(suff[j+1],arr[j])
		maxi=-1
		i=0
		j=0
		while i<n and j<n:
		    if pref[i]<=suff[j]:
		        maxi=max(maxi,j-i)
		        j+=1
		    else:
		        i+=1
	    return maxi


#{ 
 # Driver Code Starts
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		num = int(input())
		arr = [int(x) for x in input().strip().split()]
		ob = Solution()
		print(ob.maxIndexDiff(arr,num))
		t-=1
# } Driver Code Ends