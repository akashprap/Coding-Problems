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
    def accountsMerge(self, detail):
        # Code here
        n=len(detail)
        dsu=DisjointSet(n)
        mapmailnode=defaultdict(int)
        for i in range(n):
            for j in range(1,len(detail[i])):
                email=detail[i][j]
                if email not in mapmailnode:
                    mapmailnode[email]=i
                else:
                    dsu.unionBySize(i,mapmailnode[email])
        
        mergedmail=[[] for i in range(n)]
        # print(mergedmail)
        for it in mapmailnode:
            mail=it
            nod=mapmailnode[it]
            # print(mail,node)
            node=dsu.findUPar(nod)
            mergedmail[node].append(mail)
            
        ans=[]
        for i in range(n):
            if len(mergedmail[i])==0:
                continue
            else:
                mergedmail[i].sort()
                temp=[]
                temp.append(detail[i][0])
                for it in mergedmail[i]:
                    temp.append(it)
                ans.append(temp)
        return ans
            
            
            
            
            
            
            
            
            
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        accounts = []
        for i in range(n):
            cntEmails = int(input())
            nameEmails = input().split()
            accounts.append(nameEmails)
        ob = Solution()
        res = ob.accountsMerge(accounts)
        res.sort()
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            for j in range(len(res[i])):
                if j != (len(res[i]) - 1):
                    print(res[i][j], end = ', ')
                else:
                    print(res[i][j], end='')
            if (i != len(res) - 1):
                print('], ')
            else:
                print(']', end = '')
        print(']')
# } Driver Code Ends