#User function Template for python3

from typing import List

class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.size=[1]*(n+1)
        self.parent = list(range(n + 1))

    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
    

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v]+=self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u]+=self.size[ulp_v]

class Solution:
    def numOfIslands(self, n: int, m : int, operators : List[List[int]]) -> List[int]:
        # code here
        dsu=DisjointSet(n*m)
        vis=[[0]*m for i in range(n)]
        cnt=0
        ans=[]
        for row,col in operators:
            if vis[row][col]==1:
                ans.append(cnt)
                continue
            else:
                vis[row][col]=1
                cnt+=1
                dr=[-1,0,1,0]
                dc=[0,1,0,-1]
                for ind in range(4):
                    adjr=row+dr[ind]
                    adjc=col+dc[ind]
                    if adjr>=0 and adjr<n and adjc>=0 and adjc<m:
                        if vis[adjr][adjc]==1:
                            nodeno=row*m+col
                            adjnodeno=adjr*m+adjc
                            if dsu.findUPar(nodeno)!=dsu.findUPar(adjnodeno):
                                cnt-=1
                                dsu.unionBySize(nodeno,adjnodeno)
                ans.append(cnt)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        m = int(input())
        k = int(input())
        operators = []
        for i in range(k):
            u, v = map(int, input().strip().split())
            operators.append([u, v])
        obj = Solution()
        ans = obj.numOfIslands(n, m, operators)
        for i in ans:
            print(i, end = ' ')
        print()
            

# } Driver Code Ends