#User function Template for python3
import heapq as hq
class Solution:

	def kLargest(self,arr, n, k):
		# code here
		heap=[]
		hq.heapify(heap)
		for i in arr:
		    if len(heap)<k:
		        hq.heappush(heap,i)
		    else:
		        if heap[0]<i:
		          #  print(heap[0])
		            hq.heappop(heap)
		            hq.heappush(heap,i)
		        else:
		            continue
# 		print(heap)
	    ans=[]
	    while heap:
	        ans.append(hq.heappop(heap))
	    ans.sort(reverse=True)
	    return ans
		            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends