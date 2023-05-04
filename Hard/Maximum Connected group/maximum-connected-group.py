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
    def MaxConnection(self, grid : List[List[int]]) -> int:
        # code here
        n=len(grid)
        dsu=DisjointSet(n*n)
        for row in range(n):
            for col in range(n):
                if grid[row][col]==1:
                    dr=[-1,0,1,0]
                    dc=[0,1,0,-1]
                    for k in range(4):
                        nrow=row+dr[k]
                        ncol=col+dc[k]
                        if nrow>=0 and nrow<n and ncol>=0 and ncol<n and grid[nrow][ncol]==1:
                            nodeno=row*n+col
                            adjnodeno=nrow*n+ncol
                            dsu.unionBySize(nodeno,adjnodeno)
                        else:
                            continue
        maxi=0
        for row in range(n):
            for col in range(n):
                if grid[row][col]==0:
                    dr=[-1,0,1,0]
                    dc=[0,1,0,-1]
                    ans=0
                    components=set()
                    for k in range(4):
                        nrow=row+dr[k]
                        ncol=col+dc[k]
                        if nrow>=0 and nrow<n and ncol>=0 and ncol<n and grid[nrow][ncol]==1:
                            adjnodeno=nrow*n+ncol
                            components.add(dsu.findUPar(adjnodeno))
                    
                        else:
                            continue
                    for it in components:
                        ans+=dsu.size[it]
                    ans+=1
                    maxi=max(maxi,ans)
        for cells in range(0,n*n):
            maxi=max(maxi,dsu.size[dsu.findUPar(cells)])
        return maxi
                    



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        grid=IntMatrix().Input(n, n)
        
        obj = Solution()
        res = obj.MaxConnection(grid)
        
        print(res)
        

# } Driver Code Ends