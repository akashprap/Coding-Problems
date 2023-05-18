#User function Template for python3

class Solution:
    def dfs(self,i,j,vis,mat):
        vis[i][j]=1
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        for k in range(4):
            nr=i+dr[k]
            nc=j+dc[k]
            if nr>=0 and nr<len(mat) and nc>=0 and nc<len(mat[0]) and vis[nr][nc]==0 and mat[nr][nc]==1:
                self.dfs(nr,nc,vis,mat)
        
	def closedIslands(self, matrix, N, M):
		#Code here
		vis=[[0]*M for i in range(N)]
		for i in range(N):
		    if matrix[i][0]==1:
		        if not vis[i][0]:
		            self.dfs(i,0,vis,matrix)
		    if  matrix[i][M-1]==1:
		        if not vis[i][M-1]:
		            self.dfs(i,M-1,vis,matrix)
	    for i in range(M):
	        if matrix[0][i]==1:
	            if not vis[0][i]:
	                self.dfs(0,i,vis,matrix)
	        if matrix[N-1][i]==1:
	            if not vis[N-1][i]:
	                self.dfs(N-1,i,vis,matrix)
	   # print(vis)
        ans=0
        for i in range(1,N-1):
            for j in range(1,M-1):
                if matrix[i][j]==1 and vis[i][j]==0:
                    ans+=1
                    self.dfs(i,j,vis,matrix)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N, M = map(int,input().split())
        matrix = []
        for i in range(N):
            nums = list(map(int,input().split()))
            matrix.append(nums)
        obj = Solution()
        print(obj.closedIslands(matrix, N, M))
# } Driver Code Ends