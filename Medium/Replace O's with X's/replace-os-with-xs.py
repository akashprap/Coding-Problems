#User function Template for python3

class Solution:
    def dfs(self,r,c,board,vis):
        n=len(board)
        m=len(board[0])
        vis[r][c]=1
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if nr>=0 and nr<n and nc>=0 and nc<m and board[nr][nc]=="O" and vis[nr][nc]==0:
                self.dfs(nr,nc,board,vis)
    def fill(self, n, m, board):
        # code here
        vis=[[0]*m for i in range(n)]
        #first row
        for i in range(m):
            if board[0][i]=='O' and vis[0][i]==0:
                self.dfs(0,i,board,vis)
            if board[n-1][i]=='O' and vis[n-1][i]==0:
                self.dfs(n-1,i,board,vis)
        for j in range(n):
            if board[j][0]=="O" and vis[j][0]==0:
                self.dfs(j,0,board,vis)
            if board[j][m-1]=='O' and vis[j][m-1]==0:
                self.dfs(j,m-1,board,vis)
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O" and vis[i][j]==0:
                    board[i][j]="X"
        return board


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends