#User function Template for python3

class Solution:
    def isvalid(self,i,j,n,m,mat):
        if (i>=0 and i<n and j>=0 and j<m and mat[i][j]==0):
            return True
        else:
            return False
            
	def Count(self, matrix):
		# Code here
		n=len(matrix)
		m=len(matrix[0])
		dz=[[-1,0],[0,1],[1,0],[0,-1],[-1,1],[1,1],[1,-1],[-1,-1]]
		ans=0
		for i in range(n):
		    for j in range(m):
		        if matrix[i][j]==1:
    		        c=0
    		        for dr,dc in dz:
    		            if self.isvalid(i+dr,j+dc,n,m,matrix) :
    		                c+=1
    		        if (c%2==0 and c!=0):
    		          #  print(i,j)
    		            ans+=1
    		        else:
    		            ans+=0
		      
        return ans
		                
		                
		        
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.Count(matrix)
		print(ans)

# } Driver Code Ends