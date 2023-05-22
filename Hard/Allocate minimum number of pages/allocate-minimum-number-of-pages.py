class Solution:
    def ispos(self, mid, A, k):
        no_allocation = 1
        pages = 0
        for i in A:
            if i > mid:
                return False
            pages += i
            if pages > mid:
                no_allocation += 1
                pages = i
        return no_allocation <= k
        
    def books(self, A, B):
        l = max(A)
        h = sum(A)
        if B>len(A):
            return -1

        res = -1
        while l <= h:
            mid = (l + h) // 2
            if self.ispos(mid, A, B):
                res = mid
                h = mid - 1
            else:
                l = mid + 1
        return res

    def findPages(self,A, N, M):
        #code here
        return self.books(A,M)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends