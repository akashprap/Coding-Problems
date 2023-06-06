#User function Template for python3
import bisect as bs
class Solution:
    def median(self, matrix, R, C):
    	#code here
    	mini=2001
    	maxi=-1
    	for i in range(R):
    	    mini=min(mini,matrix[i][0])
    	    maxi=max(maxi,matrix[i][C-1])
    	while mini<maxi:
    	    mid=(mini+maxi)//2
    	    temp=0
    	    for i in matrix:
                temp+=bs.bisect_right(i,mid)
            if temp<(R*C+1)//2:
                mini=mid+1
            else:
                maxi=mid
        return mini
    	    
    	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends