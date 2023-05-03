#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
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
    def Solve(self, n, adj):
        # Code here
        dsu=DisjointSet(n+1)
        extraedges=0
        for u,v in adj:
            if dsu.findUPar(u)!=dsu.findUPar(v):
                dsu.unionBySize(u,v)
            else:
                extraedges+=1
        compo=0
        for i in range(n):
            if dsu.parent[i]==i:
                compo+=1
        req=compo-1
        if req<=extraedges:
            return req
        else:
            return -1
        
        
        
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        adj = [list(map(int, input().split())) for _ in range(m)]
        ob = Solution()
        res = ob.Solve(n, adj)
        print(res)
# } Driver Code Ends