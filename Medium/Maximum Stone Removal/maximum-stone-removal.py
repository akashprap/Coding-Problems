#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from collections import defaultdict
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
    def maxRemove(self, adj, n):
        # Code here
        maxrow=0
        maxcol=0
        for row,col in adj:
            maxrow=max(maxrow,row)
            maxcol=max(maxcol,col)
        dsu=DisjointSet(maxrow+maxcol+1)
        stonemap=defaultdict(int)
        for r,c in adj:
            rownode=r
            colnode=c+maxrow+1
            dsu.unionBySize(rownode,colnode)
            stonemap[rownode]=1
            stonemap[colnode]=1
        cnt=0
        for it in stonemap:
            if dsu.findUPar(it)==it:
                cnt+=1
        return n-cnt
            
            

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        adj = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        res = ob.maxRemove(adj, n)
        print(res)
# } Driver Code Ends