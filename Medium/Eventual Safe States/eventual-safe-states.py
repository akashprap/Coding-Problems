#User function Template for python3

from typing import List
from sys import setrecursionlimit
setrecursionlimit(10**6)
class Solution:
    def dfs(self,start,adj,vis,pathvis,check):
        vis[start]=1
        pathvis[start]=1
        check[start]=0
        for node in adj[start]:
            if vis[node]==0:
                if self.dfs(node,adj,vis,pathvis,check)==True:
                    check[node]=0
                    return True
            elif pathvis[node]==1:
                check[node]=0
                return True
        check[start]=1
        pathvis[start]=0
        return False
    def eventualSafeNodes(self, n: int, adj : List[List[int]]) -> List[int]:
        # code here
        vis=[0]*n
        pathvis=[0]*n
        check=[0]*n
        ans=[]
        for i in range(n):
            if not vis[i]:
                self.dfs(i,adj,vis,pathvis,check)
        for i in range(n):
            if check[i]:
                ans.append(i)
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends